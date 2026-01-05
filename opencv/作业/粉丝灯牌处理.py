import cv2

fans = cv2.imread('fans.jpeg')
i_h, i_w, _ = fans.shape
fans = cv2.resize(fans,(int(i_w / 5),  int(i_h / 5)))
bg = cv2.imread('../testb.jpg')
# 创建灰度图
fans_gray = cv2.cvtColor(fans, cv2.COLOR_BGR2GRAY)
# 创建二值图
_, fans_bin = cv2.threshold(fans_gray, 0, 255, cv2.THRESH_OTSU)
# 最外层轮廓识别
contours, hierarchy = cv2.findContours(fans_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(hierarchy.shape)
# 绘制最外层边框
# 通过RETR_TREE得到粉丝牌外框contourIdex = 1
# 绘制遮罩图
cv2.drawContours(fans_bin, contours, 1, (0, 0, 0), -1, cv2.LINE_AA)
# 取反感兴趣区域
mask = cv2.bitwise_not(fans_bin)

bit_and_fans = cv2.bitwise_and(fans, fans, mask=mask)

# 加载人脸识别模型
classifiers = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# 创建灰度图
bg_gray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
# 人脸识别
faces = classifiers.detectMultiScale(bg_gray, 1.1, 5)
print(faces)

print(mask.shape)
print(fans.shape)

fans_h, fans_w, C = fans.shape
(x, y, w, h) = faces[0]
roi = bg[y - fans_h:y, x:x + fans_w]
fans_black = cv2.bitwise_and(fans, fans, mask=mask)
roi_black = cv2.bitwise_and(roi, roi, mask=fans_bin)

res = cv2.bitwise_or(fans_black, roi_black)

bg[y - fans_h:y, x:x + fans_w] = res

cv2.imshow('win', bg)
cv2.waitKey(0)
cv2.destroyAllWindows()