import cv2
import numpy as np

def binary_dilation(img):
    # biztos bináris
    img = (img > 0).astype(np.uint8)

    padded = np.pad(img, 1, mode='constant', constant_values=0)
    h, w = img.shape
    out = np.zeros_like(img)

    for i in range(h):
        for j in range(w):

            value = 0

            for ki in range(-1, 2):
                for kj in range(-1, 2):

                    if padded[i + ki + 1, j + kj + 1] == 1:
                        value = 1
                        break

                if value == 1:
                    break

            out[i, j] = value

    return out

if __name__ == "__main__":
    img = cv2.imread("../j.ascii.pgm", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("j_binary_dilated.pgm", binary_dilation(img) * 255)

    # cv2.imwrite("eroded_cv.pgm", cv2.erode(img, np.ones((3,3), dtype=np.uint8), iterations=5))
    # cv2.imwrite("dilated_cv.pgm", cv2.dilate(img, np.ones((3,3), dtype=np.uint8), iterations=5))

    print("Dilatáció kész.")