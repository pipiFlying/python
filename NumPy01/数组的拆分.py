"""
np.split(a, indices_or_sections, axis):
    将原数组按照 0 或 1 轴平均拆成多个子数组，拆分indices_or_sections的值和的上元素必须能除尽
np.hsplit(a, indices_or_sections): 将原数组按照 1 轴平均拆成多个子数组
np.vsplit(a, indices_or_sections): 将原数组按照 0 轴平均拆成多个子数组
"""

import numpy as np

a = np.arange(1, 13).reshape(3, 4)
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""
print(a)

# axis 默认是0
b = np.split(a, 2, axis=1)
"""
[array([[ 1,  2],
       [ 5,  6],
       [ 9, 10]]), array([[ 3,  4],
       [ 7,  8],
       [11, 12]])]
"""
print(b)

c = np.split(a, 3, axis=0)
"""
[array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]])]
"""
print(c)

# [1, 2] 必须是升序，可解析成 [:1] [1:2] [2:]
d = np.split(a, [1, 2], axis=1)
"""
[array([[1],
       [5],
       [9]]), array([[ 2],
       [ 6],
       [10]]), array([[ 3,  4],
       [ 7,  8],
       [11, 12]])]
"""
print(d)