"""
过滤满足条件的数据，
    布尔索引也是深拷贝
    布尔索引也是花式索引
"""

import numpy as np

a = np.arange(1, 5)
print(a) # [1 2 3 4]

# 布尔索引必须是一个数组
print(a[[True, True, True, False]]) # [1 2 3]
print(a[True]) # [[1 2 3 4]]

print(a >= 3) # [False False  True  True]

print(a[a >= 3]) # [3, 4]


b = np.arange(1, 13).reshape(3, 4)
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""
print(b)
print(b[[True, False, True], [False, True, False, True]]) # [ 2 12]

"""
[True, False, True] 取出 
    [ 1  2  3  4]
    []
    [ 9 10 11 12]
    
[True, False, True] 等同于 [0 2]
[False, True, False, True] 等同于 [1, 3]
取交叉值 (0, 2) (1, 3)

意思就是 True 对应的就是取当前 True 在数组中的index，然后取index索引的值
"""
print(b[[0, 2], [1, 3]]) # [ 2 12]
