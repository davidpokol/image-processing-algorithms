import cv2
import numpy as np

img = cv2.imread("../lena.ascii.pgm", 0).astype(np.float32)

# --- SABLONOK (Prewitt + egyszerű derivált) ---
kx = np.array([[-1, 0, 1],
                [-1, 0, 1],
                [-1, 0, 1]], dtype=np.float32)

ky = np.array([[-1, -1, -1],
                [ 0,  0,  0],
                [ 1,  1,  1]], dtype=np.float32)

# --- konvolúció ---
gx = cv2.filter2D(img, -1, kx)
gy = cv2.filter2D(img, -1, ky)

# --- él erősség ---
edges = cv2.magnitude(gx, gy)

# --- mentés ---
cv2.imwrite("edges.pgm", np.uint8(edges))