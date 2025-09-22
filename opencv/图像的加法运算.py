"""
图像加法

因为图像有像素和色彩构成，色彩的值是 0~255 所以图像的ndarray值是uint8
最大值是 2^8 = 256 表示的数值范围就是 0~255

- 在numpy中对于uint8的加法，超出256的部分是按照模运算

- opencv 采用的是饱和运算，对于超出255的部分，直接饱和至255
    cv2.add()

** 在图像的加法运算中，要保证两张图像的大小和通道数要一致

- 图像融合
    cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None)
"""
import numpy as np
import cv2

# 在numpy中对于uint8的加法，超出256的部分是按照模运算
x = np.uint8([200])
y = np.uint8([100])

z_a = x + y
print(z_a) # [44]
print(300 % 256) # 44

# opencv 采用的是饱和运算
z_b = cv2.add(x, y)
print(z_b) # [[255]]

img_a = cv2.imread('testa.jpg')
img_b = cv2.imread('testb.jpg')

m1 = cv2.resize(img_a, (350, 500))
m2 = cv2.resize(img_b, (350, 500))

# 图像加法：必须要有相同的尺寸和通道数
img_c = cv2.add(m1, m2)

# 图像融合
# gamma > 0 图片会变亮
# gamma = 0 图片亮度不变
# gamma < 0 图片会变暗
img_d = cv2.addWeighted(m1, 0.3, img_c, 0.3, 0)

# cv2.imshow('win', img_c)
cv2.imshow('win', img_d)
cv2.waitKey(0)
cv2.destroyAllWindows()