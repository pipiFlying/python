import cv2

img = cv2.imread('testa.jpg')

# 拆分通道
b, g, r = cv2.split(img)

# cv2.imshow('win', b)
# 合并通道
img_a = cv2.merge((b, g, r))

cv2.imshow('win', img_a)
cv2.waitKey(0)
cv2.destroyWindow('win')