"""
_append: 只有Series才有该函数

insert: Series和DataFrame都有

drop: Series和DataFrame都有
"""
import numpy as np
import pandas as pd

data = np.arange(1, 13).reshape(3, 4)
df1 = pd.DataFrame(data)
"""
   0   1   2   3
0  1   2   3   4
1  5   6   7   8
2  9  10  11  12
"""
print(df1)
s1 = df1[0]
"""
0    1
1    5
2    9
Name: 0, dtype: int32
"""
print(s1)
s2 = s1._append(df1[1])
"""
0     1
1     5
2     9
0     2
1     6
2    10
dtype: int32
"""
print(s2)
# loc表示插入的位置
# column表示列标签的名字
# value插入的值可以是标量和数组
df1.insert(2, 5, np.array([100, 101, 102]))
"""
   0   1    5   2   3
0  1   2  100   3   4
1  5   6  101   7   8
2  9  10  102  11  12
"""
print(df1)

df1.drop(labels=5, axis=1, inplace=True)
"""
   0   1   2   3
0  1   2   3   4
1  5   6   7   8
2  9  10  11  12
"""
print(df1)