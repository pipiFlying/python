"""
Resample: 可选参数，指图像重采滤波器，有四种过滤方式

Image.BICUBIC: 双立方插值法
Image.NEAREST: 最近邻插值法
Image.BILINEAR: 双线性插值法
Image.LANCZOS: 下采样过滤插值法

img.split() 图像拆分

Image.transpose(method: Transpose)
"""
from PIL import Image

img = Image.open('testa.jpg')
img_a = img.resize((345, 517), resample=Image.Resampling.BICUBIC)
# img_a.show()

r, g, b = img_a.split()
# r.show()
