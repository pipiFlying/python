"""
np.random.rand(d0, d1, ..., dn) 返回一个给定形状的随机数组，随机数的范围：[0.0, 1.0)
d0, d1, ..., dn 表示形状

np.random.randint(low, light=None, size=None, dtype=int) 返回[low, high)范围的随机数
如果high=None，则返回[0, low)的随机整数。

np.random.normal(loc=0.0, scale=1.0, size=None): 返回正态分布随机数
    loc 平均值
    scale 标准差
"""

import numpy as np

# 设置随机数种子
np.random.rand(1)

a = np.random.rand(3, 4)
print(a)

b = np.random.randint(low=0, high=10, size=4)
print(b)
c = np.random.randint(low=0, high=10, size=(3, 4))
print(c)

# 正态分布随机数
d = np.random.randn(3, 4)
print(d)

e = np.random.normal(size=(3, 4))
print(e)

