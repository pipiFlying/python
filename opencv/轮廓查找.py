"""
轮廓查找
    API: contours, hierarchy = cv2.findContours(image, mode, method)
    返回值：
        contours: 轮廓的点
        hierarchy: 轮廓的层级 [[[next, previous, first_child, parent]]]
            first_child = -1 代表内层没有轮廓
            parent = -1 代表外层没有轮廓
    参数：
        mode：
            RETR_CCOMP = 2 查找的是所有轮廓，将所有轮廓组织成2层层级关系(外层轮廓和内层轮廓)
                           外层轮廓：first_child != -1, parent = -1
                           内层轮廓：first_child = -1, parent != -1
            RETR_EXTERNAL = 0 只查找最外层轮廓
            RETR_FLOODFILL = 4
            RETR_LIST = 1 查找的所有轮廓，只返回轮廓顺序关系，不返回层级关系，也就是 first_child, parent 均为 -1
            RETR_TREE = 3 查找的所有轮廓，返回轮廓顺序关系，也返回层级关系。(是最常用的方式)

        method：
            CHAIN_APPROX_NONE = 1 轮廓中的每个点都会被精确保留下来
            CHAIN_APPROX_SIMPLE = 2 仅保留轮廓的端点和拐角点

绘制轮廓
    API: cv2.drawContours(image, contours, contourIdx, color, thickness, cv2.LINE_AA)
    contourIdx: 指定轮廓的index，如果index = -1 则绘制全部轮廓
绘制轮廓，需要将绘制的图转成二值图，否则轮廓绘制不清晰
绘制二值图，需要将原图转成单通道的gary图
"""
import cv2

img = cv2.imread('outline_find.png')

# 创建单通道的gary图
img_gary = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# _: 阈值接收不要忘记
_, img_bin = cv2.threshold(img_gary, 0, 255, cv2.THRESH_OTSU)

# contours: 轮廓点
# hierarchy: 轮廓层级
contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# (1, x, 4) x 代表轮廓数
print(hierarchy.shape) # (1, 6, 4)
"""
[[[ 4 -1  1 -1]
  [-1 -1  2  0]
  [-1 -1  3  1]
  [-1 -1 -1  2]
  [ 5  0 -1 -1]
  [-1  4 -1 -1]]]
"""
print(hierarchy)

# 常规绘制轮廓
# cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

# 区分内外层轮廓绘制
for i, contour in enumerate(contours):
    # 三维数组里面取对应项
    """
    print(hierarchy.shape) # (1, 6, 4)
    
    1: 代表三维里面有一个二维数组
    6: 代表二维里面有6个一维数组
    4: 代表一维里面有4个元素
    那么可以推导 => [x, y, z]
        x: 代表二维数组的下标
        y: 代表一维数组的下标 -> 也就是0轴
        z: 代表元素的下标 -> 也就是1轴
    """
    print(hierarchy[0, i, 3])
    # 内层轮廓
    if hierarchy[0, i, 3] == -1:
        cv2.drawContours(img, contours, i, (0, 0, 255), 2)
    # 外层轮廓
    else:
        cv2.drawContours(img, contours, i, (255, 0, 0), 2)
    cv2.drawContours(img, contours, 2, (0, 0, 255), 2)

cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyWindow('win')


import numpy as np
arr = np.arange(27).reshape(3, 3, 3)  # 创建3x3x3的三维数组（0~26）
print(arr)
element = arr[1, 2, 0]  # 取第2层（i=1）、第3行（j=2）、第1列（k=0）的元素
print(element)  # 输出：15（对应数组中位置[1,2,0]的值）