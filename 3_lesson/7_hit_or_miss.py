import numpy as np
import cv2

def hit_or_miss(img, hit, miss):
    """
    img: bináris kép (0/1)
    hit: 1-ek mintája
    miss: 0-k mintája
    """

    img = (img > 0).astype(np.uint8)

    padded = np.pad(img, 1, mode='constant', constant_values=0)
    h, w = img.shape

    out = np.zeros_like(img)

    for i in range(h):
        for j in range(w):

            neighborhood = padded[i:i+3, j:j+3]

            ok_hit = np.all(neighborhood[hit == 1] == 1)
            ok_miss = np.all(neighborhood[miss == 1] == 0)

            if ok_hit and ok_miss:
                out[i, j] = 1

    return out


if __name__ == "__main__":

    hit = np.array([
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])

    miss = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0]
    ])


    img = cv2.imread("../j.ascii.pgm", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("j_hit_or_miss.pgm", hit_or_miss(img, hit, miss)* 255)

    # cv2.imwrite("eroded_cv.pgm", cv2.erode(img, np.ones((3,3), dtype=np.uint8), iterations=5))
    # cv2.imwrite("dilated_cv.pgm", cv2.dilate(img, np.ones((3,3), dtype=np.uint8), iterations=5))

    print("Hit or miss kész.")