import cv2
import numpy as np

def erosion(img):
    h, w = img.shape
    out = np.zeros_like(img)

    for i in range(1, h-1):
        for j in range(1, w-1):
            out[i,j] = np.min(img[i-1:i+2, j-1:j+2])

    return out

def dilation(image):
    h, w = image.shape
    out = np.zeros_like(image)

    for i in range(1, h - 1):
        for j in range(1, w - 1):

            neighborhood = image[i-1:i+2, j-1:j+2]
            out[i, j] = np.max(neighborhood)

    return out


if __name__ == "__main__":
    img = cv2.imread("../lena.ascii.pgm", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("eroded.pgm", erosion(img))
    cv2.imwrite("dilated.pgm", dilation(img))


    # cv2.imwrite("eroded_cv.pgm", cv2.erode(img, np.ones((3,3), dtype=np.uint8), iterations=5))
    # cv2.imwrite("dilated_cv.pgm", cv2.dilate(img, np.ones((3,3), dtype=np.uint8), iterations=5))

    print("Szürkeskálás dilatáció kész.")