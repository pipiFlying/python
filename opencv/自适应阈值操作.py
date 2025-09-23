"""
cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)--> dst:
    maxValue: 255
    adaptiveMethod: ADAPTIVE_THRESH_GAUSSIAN_C = 1
                    ADAPTIVE_THRESH_MEAN_C = 0
    thresholdType: TERM_CRITERIA_MAX_ITER = 1
                   THRESH_BINARY = 0
                   THRESH_BINARY_INV = 1
    blockSize: 需是奇数
"""
import cv2

img = cv2.imread('rose.jpg')
img = cv2.resize(img,(270, 480))

img_gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blockSize 需要时奇数
img_adap = cv2.adaptiveThreshold(img_gary, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2 )

cv2.imshow('win', img_adap)
cv2.waitKey(0)
cv2.destroyWindow('win')