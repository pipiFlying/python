import cv2
import numpy as np
from altair import param

x0, y0 = 0, 0

started = False

board = np.zeros((480, 640, 3), 'u1')

def mouse_line(event, x, y, flags, param):
    global x0, y0, started
    if event == cv2.EVENT_LBUTTONDOWN:
        x0, y0 = x, y
        started = True
    elif event == cv2.EVENT_LBUTTONUP:
        print(event)
        started = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if started:
            cv2.line(board, (x0, y0), (x, y), (0, 0, 255), 3, cv2.LINE_AA)
            x0, y0 = x, y
            cv2.imshow('win', board)

def mouse_straight_line(event, x, y, flags, param):
    global x0, y0, started
    if event == cv2.EVENT_LBUTTONDOWN:
        x0, y0 = x, y
        started = True
    elif event == cv2.EVENT_LBUTTONUP:
        started = False
        # 保存每次绘制完后的图像
        cv2.line(board, (x0, y0), (x, y), (0, 0, 255), 3, cv2.LINE_AA)
    elif event == cv2.EVENT_MOUSEMOVE and started:
        current_board = get_board()
        cv2.line(current_board, (x0, y0), (x, y), (0, 0, 255), 3, cv2.LINE_AA)
        cv2.imshow('win', current_board)

def get_board():
    return board.copy()

cv2.namedWindow('win', cv2.WINDOW_AUTOSIZE)
# cv2.setMouseCallback('win', mouse_line)
cv2.setMouseCallback('win', mouse_straight_line)
cv2.imshow('win', board)
cv2.waitKey(0)
cv2.destroyWindow('win')