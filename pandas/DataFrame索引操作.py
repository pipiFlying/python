"""
df['列标签'] - 按照列索引获取数据

DataFrame本质就是二维数组

df.loc
    先行后列就可接近numpy的处理方式(先0轴，后1轴)通过[标签索引]进行获取
df.iloc (过时了)
    先行后列就可接近numpy的处理方式(先0轴，后1轴)通过[位置索引]进行获取
"""
import numpy as np
import pandas as pd

list01 = np.arange(1, 13).reshape(3, 4)
df1 = pd.DataFrame(list01, columns=[*'abce'])
"""
   a   b   c   e
0  1   2   3   4
1  5   6   7   8
2  9  10  11  12
"""
print(df1)
"""
0    1
1    5
2    9
Name: 0, dtype: int32
"""
print(df1['a'])
print(df1['b'][0]) # 2
"""
a    1
b    2
c    3
e    4
Name: 0, dtype: int32
"""
print(df1.loc[0])
# 一下两者等效
print(df1.loc[0]['a']) # 1
print(df1.loc[0, 'a']) # 1
