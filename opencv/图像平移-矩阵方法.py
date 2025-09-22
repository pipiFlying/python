"""
[x, y] -- 笛卡尔坐标
[x, y, w] -- 齐次坐标
[x, y] -- [x/w, y/w]

平移：如果知道物体在(x, y)方向上的位移，则将其设为(tx, ty)可以创建如下矩阵
    M = 1 0 tx
        0 1 ty
w, h 为平移后的目标dst的宽高
cv2.warpAffine(src, M, (w, h))-->:dst

** 转换矩阵的元素类型必须是float32或者float64
"""
import cv2
import numpy as np

img = cv2.imread('rose.jpg')
h, w, _ = img.shape
# 平移，沿x轴平移50个像素，沿y轴平移50个像素
dx = 50
dy = 50
M = np.float32([[1, 0, dx], [0, 1, dy]])
# 平移后，如果需要图片显示完整，需要加上dx, dy
img_warp = cv2.warpAffine(img, M, (w + dx, h + dy))

cv2.imshow('win', img_warp)
cv2.waitKey(0)
cv2.destroyWindow()
