"""
下载链接
pip install opencv-contrib-python==4.6.0.66 -i https://pypi.tuna.tsinghua.edu.cn/simple/

Opencv-python 基础包

Opencv-contrib-python==4.6.0 扩展包包含了基础包
"""
import cv2
import numpy as np
from PIL import Image

# opencv无法处理中文，所以文件路径或名称不能是中文
# 读取图像，返回的是该图像对应的numpy数组
# opencv中图像形状默认是 HWC

img = cv2.imread('testa.jpg')
# print(type(img)) # <class 'numpy.ndarray'>

# 验证，opencv的颜色通道默认是 BGR
# 使用切片将每个通道获取出来
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

# 将以上的通道按照rgb组合显示
img_new = np.stack((r, g, b), axis=2)
img1 = Image.fromarray(img_new)
img1.show()
