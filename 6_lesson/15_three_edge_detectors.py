import cv2
import numpy as np

img = cv2.imread("../lena.ascii.pgm", 0).astype(np.float32)

# --- KERNELS ---

# Roberts
k1x = np.array([[1, 0],
                [0, -1]], np.float32)
k1y = np.array([[0, 1],
                [-1, 0]], np.float32)

# Prewitt
k2x = np.array([[-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]], np.float32)

k2y = np.array([[-1, -1, -1],
                [0,  0,  0],
                [1,  1,  1]], np.float32)

# Sobel (manual kernel)
k3x = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]], np.float32)

k3y = np.array([[-1, -2, -1],
                [0,  0,  0],
                [1,  2,  1]], np.float32)

# --- EDGE FUNCTION ---
def edge(img, kx, ky):
    gx = cv2.filter2D(img, -1, kx)
    gy = cv2.filter2D(img, -1, ky)
    return cv2.magnitude(gx, gy)

r = edge(img, k1x, k1y)
p = edge(img, k2x, k2y)
s = edge(img, k3x, k3y)

# --- KÜLÖNBSÉGEK ---
cv2.imwrite("diff_r_p.pgm", cv2.absdiff(r, p))
cv2.imwrite("diff_r_s.pgm", cv2.absdiff(r, s))
cv2.imwrite("diff_p_s.pgm", cv2.absdiff(p, s))

# opcionális mentés
cv2.imwrite("roberts.pgm", r)
cv2.imwrite("prewitt.pgm", p)
cv2.imwrite("sobel.pgm", s)