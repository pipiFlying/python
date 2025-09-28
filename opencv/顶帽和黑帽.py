"""
顶帽和黑帽的作用是将图像中的噪点，提取出来的操作，改为感兴趣区域

顶帽就是提取黑色里面的白色噪点
    顶帽：是输入图像和图像开运算之差
    tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

黑帽就是提取白色里的黑色噪点(但是黑色噪点，会变白)
    黑帽：是图像闭运算和原图像之差
    blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
"""
import cv2

img = cv2.imread('noise_point.png')
b_img = cv2.imread('black_noise.png')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# iterations值越高，噪点放大越明显
# 顶帽运算
tophat_img = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=5)

# iterations值越高，噪点放大越明显
# 黑帽运算
blackhat_img = cv2.morphologyEx(b_img, cv2.MORPH_BLACKHAT, kernel, iterations=5)

# cv2.imshow('win', tophat_img)
cv2.imshow('win', blackhat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
