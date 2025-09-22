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

cap = cv2.VideoCapture('hsv_test.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low, up = get_yellow_range()
    mask = cv2.inRange(hsv_frame, low, up)
    mask_img = Image.fromarray(mask)
    box = mask_img.getbbox()
    if box is not None:
        lx, ly, rx, ry = box
        cv2.rectangle(frame, (lx, ly), (rx, ry), (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)

    if cv2.waitKey(25) == 27:
        break
