import cv2

img = cv2.imread('testa.jpg')
# 创建窗口，定义窗口
# WINDOW_NORMAL: 可以修改窗口大小
# WINDOW_AUTOSIZE: 根据显示内容自动判断窗口大小

cv2.namedWindow('meinv', cv2.WINDOW_NORMAL)
# 调整窗口大小
cv2.resizeWindow('meinv', 480, 640)
# winname需与namedWindow创建的一致
cv2.imshow('meinv', img)
cv2.waitKey(0)

# 保存图像
cv2.imwrite('save_a.jpg', img)
# 不加name就是销毁全部窗口
cv2.destroyWindow('meinv')