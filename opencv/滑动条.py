"""
创建滑动条
cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
    trackbarName -- 滑动条名称
    windowName   -- 显示窗口
    value        -- 当前值
    count        -- 最大值
"""
import cv2
import numpy as np

def change(value):
    set_bg_color()

def set_bg_color():
    r = cv2.getTrackbarPos('R', 'win')
    g = cv2.getTrackbarPos('G', 'win')
    b = cv2.getTrackbarPos('B', 'win')
    board[:, :] = [b, g, r]

board = np.zeros((480, 640, 3), 'u1')
cv2.namedWindow('win', cv2.WINDOW_NORMAL)
cv2.resizeWindow('win', 640, 480)

# 创建滑动条
cv2.createTrackbar('R', 'win', 0, 255, change)
cv2.createTrackbar('G', 'win', 0, 255, change)
cv2.createTrackbar('B', 'win', 0, 255, change)


while True:
    # 在这修改。而不通过change回调函数修改，可解决如果滑动条有初始值时触发，change，而此时后面滑到还没有创建
    # 而cv2.getTrackbarPos('G', 'win')已经开始获取，而报错
    # set_bg_color()
    cv2.imshow('win', board)
    if cv2.waitKey(1) == 27:
        break

cv2.destroyWindow('win')