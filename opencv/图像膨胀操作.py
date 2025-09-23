import cv2
import numpy as np

img = cv2.imread('fushi_test.png')
# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
# 腐蚀操作，去掉不需要的部分
erode_img = cv2.erode(img, kernel, iterations=10)

# 膨胀操作，还原被腐蚀操作缩小的需要恢复的部分
dilate_img = cv2.dilate(erode_img, kernel, iterations=10)

res = np.hstack((img, dilate_img))
erode_img_res = np.hstack((img, erode_img))
cv2.imshow('win', res)
# cv2.imshow('win', erode_img_res)
cv2.waitKey(0)
cv2.destroyWindow('win')