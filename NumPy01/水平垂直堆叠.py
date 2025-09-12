"""
数组水平垂直堆叠：
    水平堆叠使用 hstack 相当于concatenate 函数 axis=1
    垂直堆叠使用 vstack 相当于concatenate 函数 axis=0
"""
import numpy as np

m = np.array([[1, 2], [3, 4]])
n = np.array([[5, 6], [7, 8]])

k = np.hstack((m, n))
"""
[[1 2 5 6]
 [3 4 7 8]]
"""
print(k)
l = np.vstack((m, n))
"""
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""
print(l)
