"""
多维数组迭代是相对于第一个轴完成的

如果想要对数组中的每个元素执行操作，可以使用迭代器
    np.nditer(b)
"""

import numpy as np

a = np.arange(1, 13).reshape(3, 4)
"""
[[1 2 3 4]
 [5 6 7 8]
 [9 10 11 12]]
"""

for i in a:
    print(i)
"""
[1 2 3 4]
[5 6 7 8]
[ 9 10 11 12]
"""

for e in np.nditer(a):
    print(e)