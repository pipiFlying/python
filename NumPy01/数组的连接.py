"""
连接数组
np.concatenate():
    axis 指定拼接轴方向
    concatenate((a1, a2, ...), axis=0)
    要求对应轴精确匹配
"""

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))
print(c)

d = np.arange(1, 13).reshape(3, 4)
e = np.arange(11, 23).reshape(3, 4)

# axis 指定拼接方向，axis 默认是 0轴
f = np.concatenate((d, e))
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [11 12 13 14]
 [15 16 17 18]
 [19 20 21 22]]
"""
print(f)

# 指定按照1轴拼接
g = np.concatenate((d, e), axis=1)
"""
[[ 1  2  3  4 11 12 13 14]
 [ 5  6  7  8 15 16 17 18]
 [ 9 10 11 12 19 20 21 22]]
"""
print(g)

h = np.array([[1, 2], [3, 4]])
i = np.array([[5, 6]])
j = np.concatenate((h, i))
print(j)