"""
s.loc(标签索引 / 切片 / 函数): 根据给定的标签索引或布尔索引获取元素

s.iloc(位置索引 / 切片): 根据给定的位置索引或布尔索引获取元素
    这里的i表示的是整数位置索引，i = integer

s.head(num):
    默认获取前5个
    num传入就是获取前num个

s.tail(num):
    默认获取后5个
    num传入就是获取后num个
"""
import pandas as pd
import numpy as np

data = np.array([11, 12, 13, 14, 15, 16, 17])
s1 = pd.Series(data)
s2 = pd.Series(data, index=[*'abcdefg'])
print(s1)
print(s2.loc['a':'c'])
print(s2.loc[['a', 'c']])
print(s2.loc[[True, False, True, False, True, False, False]])

x = s1.loc[lambda e: e > 12]
print(x)
"""
0    11
1    12
dtype: int32
"""
print(s1.head(2))
"""
5    16
6    17
dtype: int32
"""
print(s1.tail(3))