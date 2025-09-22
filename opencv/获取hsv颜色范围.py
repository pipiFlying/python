import cv2
import numpy as np

# 创建一个蓝色像素
# 维度为3表示三通道
blue = np.uint8([[[255, 0, 0]]])

# 将BGR转成HSV
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
# 计算yellow的hsv范围
# [H-10, 100, 100]和[H+10, 255, 255]
# hsv_blue[0, 0, 0]末尾的0表示0, 1, 2 的第0个通道
hsv_blue_low = (hsv_blue[0, 0, 0] - 10, 100, 100)
hsv_blue_up = (hsv_blue[0, 0, 0] + 10, 255, 255)

print(hsv_blue_low)
print(hsv_blue_up)