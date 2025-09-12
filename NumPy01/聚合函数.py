"""
np.sum() 求和
np.amax() 最大值
np.amin() 最小值
np.mean() 平均值
np.average() 加权平均值
np.argmax() 最大值索引

聚合函数默认情况下，按照哪一个轴进行聚合，哪一个轴就会消失。
结果就是降维
"""
import numpy as np

a = np.arange(1, 13).reshape(3, 4)
"""
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
"""
print(a)
b = np.sum(a, axis=0)
b2 = np.sum(a, axis=1)
b3 = np.sum(a)
print(b, b2, b3) # [15 18 21 24] [10 26 42] 78
