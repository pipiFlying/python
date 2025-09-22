"""
opencv图像的颜色空间是：BGR

图像空间转换方法：
    cv2.cvtColor(img, code)
    常用值
    code = COLOR_BGR2RGB = 4
           COLOR_BGR2RGBA = 2
           COLOR_BGR2HSV = 40
           ...

HSV
    H - 色相 (Hue色相用0~360度数字表示) ** 但是在numpy中是0~180 红色除外
    S - 饱和度
    V - 亮度

"""
import cv2
import numpy as np

# 创建一个蓝色像素
# 维度为3表示三通道
blue = np.uint8([[[255, 0, 0]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)

print(hsv_blue)