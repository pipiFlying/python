"""
按位与
    cv2.bitwise_and

0 是黑色 255 是白色

    按位与
    0 & color = 0
    255 & color = color

    按位或
    0 | color = color
    255 | color = 255
"""
import cv2
import numpy as np

img = cv2.imread('testa.jpg')
h, w, _ = img.shape

# 制作掩码图
# 掩码图一般是单通道
mask = np.zeros((h, w), 'u1')

# 绘制需要显示的圆形区域
cv2.circle(mask, (310, 330), 100, (255, 255, 255), -1, cv2.LINE_AA)

# 将掩码图和原图做位运算得到RIO(感兴趣区域)
dst = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('win', dst)
cv2.waitKey(0)
cv2.destroyWindow('win')