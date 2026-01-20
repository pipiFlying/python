import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
image[:, 250:] = 255

cv2.imshow('window', image)
cv2.waitKey(0)
cv2.destroyWindow('window')