import numpy as np
import pandas as pd
from rope.base.oi.type_hinting.evaluate import prefix

data01 = np.arange(1, 13).reshape(3, 4)
df1 = pd.DataFrame(data01)
"""
   0   1   2   3
0  1   2   3   4
1  5   6   7   8
2  9  10  11  12
"""
print(df1)

# 转置
"""
   0  1   2
0  1  5   9
1  2  6  10
2  3  7  11
3  4  8  12
"""
print(df1.T)

# 增加
df1[4] = [5, 9, 13]
df1.loc[3] = [13, 14, 15, 16, 17]
"""
    0   1   2   3   4
0   1   2   3   4   5
1   5   6   7   8   9
2   9  10  11  12  13
3  13  14  15  16  17
"""
print(df1)

# 删除
del df1[4]
"""
   0   1   2   3
0  1   2   3   4
1  5   6   7   8
2  9  10  11  12
"""
print(df1)

s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)
s2 = s1.reindex(index=[1, 2, 3])
"""
1    2
2    3
3    4
dtype: int64
"""
print(s2)
s3 = s1.reindex(index=[1, 2, 3, 6])
"""
1    2.0
2    3.0
3    4.0
6    NaN
dtype: float64
"""
print(s3)
s4 = s1.reindex(index=[*'abcde'])
"""
a   NaN
b   NaN
c   NaN
d   NaN
e   NaN
dtype: float64
"""
print(s4)

np_arr = np.arange(1, 13).reshape(3, 4)
df1 = pd.DataFrame(np_arr)
"""
   0   1   2   3
0  1   2   3   4
1  5   6   7   8
2  9  10  11  12
"""
print(df1)
# labels设置的是行或列的索引名称，取决于axis轴
df_s1 = df1.reindex(labels=[0, 1, 2], axis=1)
"""
   0   1   2
0  1   2   3
1  5   6   7
2  9  10  11
"""
print(df_s1)
df_s2 = df1.reindex(columns=[0, 1, 2])
"""
   0   1   2
0  1   2   3
1  5   6   7
2  9  10  11
"""
print(df_s2)
df_s3 = df1.reindex(columns=[*'abc'])
"""
    a   b   c
0 NaN NaN NaN
1 NaN NaN NaN
2 NaN NaN NaN
"""
print(df_s3)
df_s4 = df1.reindex(columns=[*'abc'], fill_value=888)
"""
     a    b    c
0  888  888  888
1  888  888  888
2  888  888  888
"""
print(df_s4)

