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
        img = np.array(data, dtype=np.float64).reshape((height, width))

    return img, max_val


def write_pgm(filename, image, max_val=255):
    height, width = image.shape

    with open(filename, 'w') as f:
        f.write('P2\n')
        f.write(f'{width} {height}\n')
        f.write(f'{max_val}\n')

        for row in image:
            f.write(' '.join(map(str, row)) + '\n')

def load_images(file_list):
    images = []
    max_val = None

    for fname in file_list:
        img, mv = read_pgm(fname)

        if max_val is None:
            max_val = mv
        else:
            assert mv == max_val, "Eltérő max_val!"

        images.append(img)

    shapes = [img.shape for img in images]
    assert len(set(shapes)) == 1, "A képek mérete nem egyezik!"

    return np.stack(images), max_val

def average_image(images):
    return np.mean(images, axis=0)

def median_image(images):
    return np.median(images, axis=0)

if __name__ == "__main__":
    input_files = [
        "../lena.ascii.pgm",
        "../barbara.ascii.pgm",
        "../baboon.ascii.pgm",
    ]

    avg_output = "lena-barbara-baboon-average.pgm"
    med_output = "lena-barbara-baboon-median.pgm"

    images, max_val = load_images(input_files)

    avg_img = average_image(images)
    med_img = median_image(images)

    write_pgm(avg_output, avg_img, max_val)
    write_pgm(med_output, med_img, max_val)

    print("Átlag és medián képek elkészültek.")