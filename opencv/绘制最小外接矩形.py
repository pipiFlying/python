"""
绘制最小外接矩形
1. 获取图像轮廓
2. 传入轮廓得到最小外接矩形 -- box = cv2.minAreaRect(contours[index])
3. 获取最小外接矩形的四个角坐标 -- points = cv2.boxPoints(box)
4. 使用绘制轮廓的方法绘制最小外接矩形
    a. points必须升3维
    b. points中的元素必须是int32或int64
"""
import cv2
import numpy as np

img = cv2.imread('bounding_rectangle.png')
# 获取单通道灰色图
img_gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 获取二值图
_, img_bin = cv2.threshold(img_gary, 0, 255, cv2.THRESH_OTSU)
# 获取图像轮廓
contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# 将轮廓交给minAreaRect函数，得到最小外接矩形
# 返回值：(中心(x, y), (宽, 高), 旋转角度)
box = cv2.minAreaRect(contours[0])
# 获取最小外接矩形的四个点坐标
points = cv2.boxPoints(box)
# 用绘制轮廓的方法绘制最小外接矩形
"""
绘制轮廓时，contours必须是三维的, points是二维需要升维
且contours必须是int32或int64类型整数，points是浮点数需要类型转换
"""
int_points = np.intp(points)
cv2.drawContours(img, [int_points], -1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()