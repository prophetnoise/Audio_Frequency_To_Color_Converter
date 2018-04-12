import frq_to_rgb
import cv2
import numpy as np

# cv2 uses BGR instead of RGB
# Convert RGB to BGR
def rgb_to_bgr(RGB):
    BGR = (RGB[::-1])
    return BGR

def create_image(BGR):
    image = np.zeros((1000,1000,3), np.uint8)
    image[::] = BGR
    return image


BGR = rgb_to_bgr(frq_to_rgb.RGB)
image = create_image(BGR)
cv2.imshow('Color Octave',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
