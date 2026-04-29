# Küszöbölés
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

def threshold_image(image, thresholds, max_val=255):
    thresholds = sorted(thresholds)
    levels = len(thresholds) + 1

    # kimeneti kép
    result = np.zeros_like(image, dtype=np.uint8)

    # szintek kiszámítása
    step = max_val // (levels - 1) if levels > 1 else max_val

    for i, t in enumerate(thresholds):
        result[image >= t] = (i + 1) * step

    return result

if __name__ == "__main__":
    input_file = "../lena.ascii.pgm"
    output_file = "lena_tresholded.pgm"

    kernel_size = 5      # 3, 5 vagy 7
    mode = "ignore"      # "valid", "zero", "ignore"

    img, max_val = read_pgm(input_file)

    result = threshold_image(img, [128], max_val)

    write_pgm(output_file, result, max_val)

    print("Küszöbölés kész.")