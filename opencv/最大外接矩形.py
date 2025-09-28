"""
最大外接矩形
    API: cv2.boundingRect(array)
        array: 轮廓点位坐标
"""
import cv2

img = cv2.imread('bounding_rectangle.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

box = cv2.boundingRect(contours[0])
# 得到左上角坐标和矩形宽高
x, y, w, h = box
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()