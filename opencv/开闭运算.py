"""
开运算：
    先腐蚀再膨胀
闭运算：
    先膨胀再腐蚀

操作API
cv2.morphologyEx(src, op, kernel)
    src: 操作图像
    op: 开运算或者闭运算
        cv2.MORPH_OPEN
        cv2.MORPH_CLOSE
    kernel: 结构元素
"""
import cv2
import numpy as np

img = cv2.imread('fushi_test.png')
# 创建结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

res = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)

cv2.imshow('win', res)
cv2.waitKey(0)
cv2.destroyWindow('win')
