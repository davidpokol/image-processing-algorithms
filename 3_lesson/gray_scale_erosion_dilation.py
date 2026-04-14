import cv2
import numpy as np

def erosion(img, iterations=1):

    out = img.copy()

    for _ in range(iterations):

        padded = np.pad(out, 1, mode='edge')
        h, w = out.shape
        new_img = np.zeros_like(out)

        for i in range(h):
            for j in range(w):

                min_val = 255

                for ki in range(-1, 2):
                    for kj in range(-1, 2):

                        val = padded[i + ki + 1, j + kj + 1]
                        if val < min_val:
                            min_val = val

                new_img[i, j] = min_val

        out = new_img

    return out

def dilation(image, iterations=1):
    out = image.copy()

    for _ in range(iterations):

        padded = np.pad(out, 1, mode='edge')
        h, w = out.shape
        new_img = np.zeros_like(out)

        for i in range(h):
            for j in range(w):

                max_val = 0

                for ki in range(-1, 2):
                    for kj in range(-1, 2):

                        val = padded[i + ki + 1, j + kj + 1]
                        if val > max_val:
                            max_val = val

                new_img[i, j] = max_val

        out = new_img

    return out

def erosion_no_iteration(img):
    h, w = img.shape
    out = np.zeros_like(img)

    for i in range(1, h-1):
        for j in range(1, w-1):
            out[i,j] = np.min(img[i-1:i+2, j-1:j+2])

    return out

def dilation_no_iteration(image):
    h, w = image.shape
    out = np.zeros_like(image)

    for i in range(1, h - 1):
        for j in range(1, w - 1):

            neighborhood = image[i-1:i+2, j-1:j+2]
            out[i, j] = np.max(neighborhood)

    return out


if __name__ == "__main__":
    img = cv2.imread("../lena.ascii.pgm", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("eroded.pgm", erosion(img, iterations=5))
    cv2.imwrite("dilated.pgm", dilation(img, iterations=5))


    # cv2.imwrite("eroded_cv.pgm", cv2.erode(img, np.ones((3,3), dtype=np.uint8), iterations=5))
    # cv2.imwrite("dilated_cv.pgm", cv2.dilate(img, np.ones((3,3), dtype=np.uint8), iterations=5))

    print("Szűrés kész.")