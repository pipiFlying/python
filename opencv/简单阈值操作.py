"""
- 在进行图像处理的时候，大多数时候需要将彩色图像转成灰度图像或者二值图像。
- 在图像的形态学操作中，也主要是对二值图像进行形态学的相关操作。
- OpenCV中图像阈值分为：简单阈值(全局阈值)和自适应阈值

cv2.threshold(src, thresh, maxval, type)
    type: 常用参数
        THRESH_BINARY = 0
        THRESH_BINARY_INV = 1
        THRESH_OTSU = 8
"""
import cv2

img = cv2.imread('rose.jpg')
img = cv2.resize(img,(270, 480))
# 将原始图像进行阈值处理，得到二值图像
# 1. 现将图像转灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 输出值域图
x, img_gray_THRESH = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
# x 就是输出的阈值
print(x)

cv2.imshow('win', img_gray_THRESH)
cv2.waitKey(0)
cv2.destroyWindow()