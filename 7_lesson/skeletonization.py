import cv2
import numpy as np

def skeletonize_pgm(input_path, output_path):
    # 1. Load the PGM P2 file
    # OpenCV's imread handles PGM P2 and P5 automatically
    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print("Error: Could not open image.")
        return

    # 2. Binarize the image 
    # Skeletonization requires a binary image (0 and 255)
    # Using Otsu's thresholding to find the best split point
    ret, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # 3. Initialize the skeleton as an empty black image
    skeleton = np.zeros(binary.shape, np.uint8)
    
    # 4. Get a cross-shaped structuring element (3x3)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    
    done = False
    temp_img = binary.copy()

    # 5. Iterative Morphological Thinning
    while not done:
        # Erosion shrinks the white foreground
        eroded = cv2.erode(temp_img, element)
        # Opening (Erosion followed by Dilation) finds the "main body"
        temp = cv2.dilate(eroded, element)
        # Subtracting the "opened" version from the original finds the "edges" or "ends"
        temp = cv2.subtract(temp_img, temp)
        # Add the extracted edges to the skeleton
        skeleton = cv2.bitwise_or(skeleton, temp)
        # Update temp_img for the next iteration
        temp_img = eroded.copy()

        # If there are no more white pixels left to erode, we are done
        if cv2.countNonZero(temp_img) == 0:
            done = True

    # 6. Save result back to PGM (OpenCV defaults to P5 for PGM; 
    # to force P2, you'd need a custom write function, 
    # but P5 is the standard binary equivalent)
    cv2.imwrite(output_path, skeleton)
    print(f"Skeletonization complete. Saved to {output_path}")

# Example Usage
skeletonize_pgm('../plant.ascii.pgm', 'skeleton_output.pgm')