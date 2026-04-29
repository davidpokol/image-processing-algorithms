import numpy as np

def read_pgm(filename):
    with open(filename, 'r') as f:
        assert f.readline().strip() == 'P2'

        line = f.readline()
        while line.startswith('#'):
            line = f.readline()

        width, height = map(int, line.split())
        max_val = int(f.readline().strip())

        data = []
        for line in f:
            if line.startswith('#'):
                continue
            data.extend([int(x) for x in line.split()])
        image = np.array(data, dtype=np.uint8).reshape((height, width))

    return image, max_val


def write_pgm(filename, image, max_val=255):
    height, width = image.shape

    with open(filename, 'w') as f:
        f.write('P2\n')
        f.write(f'{width} {height}\n')
        f.write(f'{max_val}\n')

        for row in image:
            f.write(' '.join(map(str, row)) + '\n')


# ---------- Medián szűrő ----------

def median_filter(image, kernel_size=3, mode="ignore"):
    assert kernel_size in [3, 5, 7]
    assert mode in ["valid", "zero", "ignore"]

    pad = kernel_size // 2
    h, w = image.shape

    if mode == "valid":
        out_h = h - 2 * pad
        out_w = w - 2 * pad
        output = np.zeros((out_h, out_w))

        for i in range(out_h):
            for j in range(out_w):
                window = image[i:i+kernel_size, j:j+kernel_size]
                output[i, j] = np.median(window)

        return output

    elif mode == "zero":
        padded = np.pad(image, pad, mode='constant', constant_values=0)
        output = np.zeros_like(image)

        for i in range(h):
            for j in range(w):
                window = padded[i:i+kernel_size, j:j+kernel_size]
                output[i, j] = np.median(window)

        return output

    elif mode == "ignore":
        output = np.zeros_like(image)

        for i in range(h):
            for j in range(w):
                i_min = max(i - pad, 0)
                i_max = min(i + pad + 1, h)
                j_min = max(j - pad, 0)
                j_max = min(j + pad + 1, w)

                window = image[i_min:i_max, j_min:j_max]
                output[i, j] = np.median(window)

        return output

# ---------- MAIN ----------

if __name__ == "__main__":
    input_file = "../lena.ascii.pgm"
    output_file = "lena_median_filtered.pgm"

    kernel_size = 7      # 3, 5, 7
    mode = "ignore"      # "valid", "zero", "ignore"

    img, max_val = read_pgm(input_file)

    result = median_filter(img, kernel_size, mode)

    write_pgm(output_file, result, max_val)

    print("Medián szűrés kész.")