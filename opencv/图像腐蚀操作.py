import cv2
import numpy as np

img = cv2.imread('fushi_test.png')

# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

# iterations 腐蚀次数越多，噪点消除更明显，但是会缩小感兴趣区域，次数越多，缩小越明显
erode_img = cv2.erode(img, kernel, iterations=2)
# 图片堆叠，对比腐蚀效果
res = np.hstack((img, erode_img))

cv2.imshow('win', res)
cv2.waitKey(0)
cv2.destroyWindow('win')