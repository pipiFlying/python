"""
要捕获视频，需要创建一个VideoCapture对象，它的参数可以是设备索引或视频文件的名称
设备索引就是指定哪个摄像头数字。正常情况下，一个摄像头会被连接。所以可以简单的传0或-1
你可以通过传递1来选择第二个相机，以此类推，在此之后，你可以逐帧捕获。

最后需要释放资源

视频 = 一帧一帧的图像
"""
import cv2

cap = cv2.VideoCapture(0)
# print(cap.isOpened())

# 从摄像头中读取图像
while cap.isOpened():
    # read: 读取视频帧，返回两个值：是否读取成功，读取到图像
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
        code = cv2.waitKey(25)
        if code == ord('q') or code == 27:
            break

# 释放摄像头资源
cap.release()

# 关闭窗口
# cv2.destroyWindow('frame')