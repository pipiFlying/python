import cv2

# 传入视频文件路径
cap = cv2.VideoCapture('video_t.mp4')

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# 设置窗口并调整大小
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', int(w // 4), int(h // 4))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('video', frame)
    if cv2.waitKey(25) == ord('q') or cv2.waitKey(0) == 27:
        break

# 释放资源
cap.release()
cv2.destroyWindow('video')