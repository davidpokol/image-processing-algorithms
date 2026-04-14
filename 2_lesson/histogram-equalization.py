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
            data.extend(map(int, line.split()))
        img = np.array(data, dtype=np.uint8).reshape((height, width))

    return img, max_val

def write_pgm(filename, image, max_val=255):
    height, width = image.shape

    with open(filename, 'w') as f:
        f.write('P2\n')
        f.write(f'{width} {height}\n')
        f.write(f'{max_val}\n')

        for row in image:
            f.write(' '.join(map(str, row)) + '\n')


def histogram_equalization(image, max_val=255):
    # Flatten image
    flat = image.flatten()

    # Histogram
    hist = np.bincount(flat, minlength=max_val + 1)

    # Normalize histogram (PDF)
    pdf = hist / np.sum(hist)

    # Cumulative distribution function (CDF)
    cdf = np.cumsum(pdf)

    # Normalize CDF to [0, max_val]
    cdf_scaled = np.floor(cdf * max_val).astype(np.uint8)

    # Map pixels
    equalized = cdf_scaled[flat]

    return equalized.reshape(image.shape)


if __name__ == "__main__":
    input_file = "../lena.ascii.pgm"
    output_file = "lena_equalized.pgm"

    image, max_val = read_pgm(input_file)

    result = histogram_equalization(image, max_val)

    write_pgm(output_file, result, max_val)

    print("Histogram equalization done.")