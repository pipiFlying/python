"""
numpy 中元素使用基本运算符是对位运算

如果使用 *= 或 += 则会就地修改数组不会创建新的数组

numpy 除了可以使用基本运算符外，numpy 还提供了运算函数
加法
    np.add(a, b)
减法
    np.subtract(a, b)
乘法
    np.multiply(a, b)
除法
    地板除，整除
    np.floor_divide(a, b)
    任意除
    np.divide(a, b)
"""
import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(1, 7).reshape(2, 3)
"""
[[ 1  4  9]
 [16 25 36]]
"""
print(a * b)

"""
[[ 2  4  6]
 [ 8 10 12]]
"""
print(np.add(a, b))

print(np.subtract(a, b))