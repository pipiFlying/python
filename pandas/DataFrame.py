"""
Series转DataFrame
    方式一: pd.DataFrame(s)
    方式二: s.to_frame()
"""
import numpy as np
import pandas as pd

data = np.array([1, 2, 3, 4, 5])
s1 = pd.Series(data)
"""
0    1
1    2
2    3
3    4
4    5
dtype: int32
"""
print(s1)
# Series转DataFrame的时候，index的值如果是Series的标签索引，就会过去对应的值：否则就是NaN
# columns设置的就是列索引：
# 1. 如果Series设置name,此时没有显示的指定colums,列索引的名称就是Series的name
# 2. 如果Series没有设置name,此时没有显示的指定colums,列索引的名称就是从0开始的值
# 3. 显示的指定colums,列索引的名称就是指定的值
df1 = pd.DataFrame(s1)
"""
   0
0  1
1  2
2  3
3  4
4  5
"""
print(df1)
# 使用s.to_frame()
df2 = s1.to_frame()
"""
   0
0  1
1  2
2  3
3  4
4  5
"""
print(df2)

dict01 = {
    'aa': [1, 2, 3, 4, 5],
    'bb': np.array([11, 12, 13, 14, 15]),
    'cc': (111, 112, 113, 114, 115),
    'dd': pd.Series(data=[1111, 1112, 1113, 1114, 1115])
}
df3 = pd.DataFrame(dict01)
"""
   aa  bb   cc    dd
0   1  11  111  1111
1   2  12  112  1112
2   3  13  113  1113
3   4  14  114  1114
4   5  15  115  1115
"""
print(df3)
print(df3['aa'])

dict02 = {
    'info1': {
        'id': 1,
        'name': 'tom',
        'age': 23,
    },
    'info2': {
        'id': 2,
        'name': 'jim',
        'age': 30,
    }
}
# 先当列再当行
df4 = pd.DataFrame(dict02)
"""
     info1 info2
id       1     2
name   tom   jim
age     23    30
"""
print(df4)
# 操作数组数据
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
]
df5 = pd.DataFrame(arr)
"""
   0  1  2  3   4
0  1  2  3  4   5
1  6  7  8  9  10
"""
print(df5)
# 操作numpy二维数组
np_arr = np.arange(1, 13).reshape(3, 4)
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""
print(np_arr)
df6 = pd.DataFrame(np_arr)
"""
   0   1   2   3
0  1   2   3   4
1  5   6   7   8
2  9  10  11  12
"""
print(df6)