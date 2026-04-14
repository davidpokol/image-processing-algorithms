import cv2
import numpy as np

def band_filter(shape, D1, D2, bandstop=False):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2

    H = np.zeros((rows, cols), dtype=np.float32)

    for u in range(rows):
        for v in range(cols):
            D = np.sqrt((u - crow)**2 + (v - ccol)**2)

            if bandstop:
                H[u, v] = 0 if D1 <= D <= D2 else 1
            else:
                H[u, v] = 1 if D1 <= D <= D2 else 0

    return H


def apply_band_filter(input_path, output_path, D1, D2, bandstop=False):
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # DFT
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # maszk
    H = band_filter(img.shape, D1, D2, bandstop)
    H = np.stack((H, H), axis=-1)

    # szűrés
    filtered = dft_shift * H

    # vissza
    f_ishift = np.fft.ifftshift(filtered)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])

    # normalizálás (PGM!)
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    img_back = np.uint8(img_back)

    cv2.imwrite(output_path, img_back)


# ===== használat =====

# sáváteresztő
apply_band_filter("../lena.ascii.pgm", "bandpass.pgm", 20, 50, bandstop=False)

# sávzáró
apply_band_filter("../lena.ascii.pgm", "bandstop.pgm", 20, 50, bandstop=True)