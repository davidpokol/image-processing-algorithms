import cv2
import numpy as np

def rectangle_orientation(image_path):
    # 1. kép beolvasása
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 2. élkeresés
    edges = cv2.Canny(img, 50, 150)

    # 3. Hough-transzformáció
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

    if lines is None:
        return None

    angles = []

    # 4. szögek kigyűjtése
    for rho, theta in lines[:, 0]:
        # Hough theta → normál irány, ezért -90°
        angle = theta - np.pi / 2
        angle_deg = np.rad2deg(angle)

        # normalizálás -90..90 közé
        if angle_deg < -90:
            angle_deg += 180
        if angle_deg > 90:
            angle_deg -= 180

        angles.append(angle_deg)

    # 5. domináns irány (medián)
    orientation = np.median(angles)

    return orientation

# használat
angle = rectangle_orientation("../rectangle.ascii.pgm")

if angle is not None:
    print(f"Téglalap iránya: {angle:.2f} fok")
else:
    print("Nem találtunk egyeneseket.")