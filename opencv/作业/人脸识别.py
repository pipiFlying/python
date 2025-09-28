import cv2

img = cv2.imread('../testb.jpg')
# 记载人脸识别模型
classifiers = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 创建灰度图
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 人脸检测
# scaleFactor缩放因子必须 > 1, 默认值是1.1, 一般使用 1.1 ~ 1.5
# scaleFactor=1.3 表示图像缩放成：原图 / 1.3
# scaleFactor越大，检测效率越快，可能会漏检误检
# minNeighbors：表示检测人脸的时候周边num个区域都有人脸特征信息
faces = classifiers.detectMultiScale(img_gray, 1.1, 5)
if faces is not None:
    for (x, y, w, h) in faces:
        # 绘制人脸识别区域
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()