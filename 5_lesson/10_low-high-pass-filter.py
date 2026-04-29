import cv2
import numpy as np

def ideal_filter(shape, D0, highpass=False):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2

    H = np.zeros((rows, cols), dtype=np.float32)

    for u in range(rows):
        for v in range(cols):
            D = np.sqrt((u - crow)**2 + (v - ccol)**2)

            if highpass:
                H[u, v] = 1 if D > D0 else 0
            else:
                H[u, v] = 1 if D <= D0 else 0

    return H


def process_pgm(input_path, output_path, D0, highpass=False):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # DFT
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # maszk
    H = ideal_filter(img.shape, D0, highpass)
    H = np.stack((H, H), axis=-1)

    # szűrés
    filtered = dft_shift * H

    # vissza
    f_ishift = np.fft.ifftshift(filtered)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])

    # normalizálás 0–255-re (PGM-hez fontos!)
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    img_back = np.uint8(img_back)

    cv2.imwrite(output_path, img_back)


# ===== használat =====

process_pgm("../lena.ascii.pgm", "lowpass.pgm", D0=30, highpass=False)
process_pgm("../lena.ascii.pgm", "highpass.pgm", D0=30, highpass=True)