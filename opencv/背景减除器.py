"""
背景减除器
    API: cv2.createBackgroundSubtractorMOG2()
    作用：捕捉移动画面，一般常用语流动物体抓拍捕获
"""
import cv2

cap = cv2.VideoCapture('traffic.mp4')

# 创建背景减除器
bg_sub = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 创建灰度图
    frame_gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 创建二值图
    _, frame_bin = cv2.threshold(frame_gary, 0, 255, cv2.THRESH_OTSU)
    # 实际使用中灰度图和二值图需要测试，才决定用哪个
    mask = bg_sub.apply(frame_gary)
    cv2.imshow('frame', mask)
    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()