import cv2

cap = cv2.VideoCapture('../traffic.mp4')
bg_sub = cv2.createBackgroundSubtractorMOG2()
# 创建结构元素
kernel_o = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
kernel_c = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        roi = frame[200:, 0:1400]
        roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, roi_bin = cv2.threshold(roi_gray, 0, 255, cv2.THRESH_OTSU)
        sub_frame = bg_sub.apply(roi_gray)
        # 进行图像开运算
        res = cv2.morphologyEx(sub_frame, cv2.MORPH_OPEN, kernel_o, iterations=2)
        res = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel_c, iterations=6)
        # 获取轮廓
        contours, hierarchy = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # # 得到左上角坐标和矩形宽高
        for c in contours:
            if c is not None:
                x, y, w, h = cv2.boundingRect(c)
                if 40 <= w and 40 <= h:
                    cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 2, cv2.LINE_AA)

        # cv2.imshow('res', res)
        cv2.imshow('res', roi)

    if cv2.waitKey(25) == 27:
        break

cap.release()
cv2.destroyAllWindows()