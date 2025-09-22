"""
1. 计算yellow的hsv范围
2. 制作掩码图
3. 获取yellow边界坐标
4. 绘制边框
"""
import cv2
import numpy as np
from PIL import Image

def get_yellow_range():
    # 创建一个蓝色像素
    # 维度为3表示三通道
    yellow = np.uint8([[[0, 255, 255]]])

    # 将BGR转成HSV
    hsv_yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
    # 计算yellow的hsv范围
    # [H-10, 100, 100]和[H+10, 255, 255]
    # hsv_yellow[0, 0, 0]末尾的0表示0, 1, 2 的第0个通道
    hsv_blue_low = (hsv_yellow[0, 0, 0] - 10, 100, 100)
    hsv_blue_up = (hsv_yellow[0, 0, 0] + 10, 255, 255)
    return np.uint8(hsv_blue_low), np.uint8(hsv_blue_up)

img = cv2.imread('hsv_test.png')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 制作掩码图
low, up = get_yellow_range()
mask = cv2.inRange(img_hsv, low, up)

# 将mask转成Image
mask_img = Image.fromarray(mask)
# getbbox(): 获取非0区域的边界坐标，左上角和右下角的坐标
box = mask_img.getbbox()
if box is not None:
    lx, ly, rx, ry = box
    cv2.rectangle(img, (lx, ly), (rx, ry), (0, 0, 255), 2, cv2.LINE_AA)

cv2.namedWindow('win', cv2.WINDOW_AUTOSIZE)
cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()