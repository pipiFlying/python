"""
np.sort(arr, axis=-1, kind=None, order=None)
    kind排序类型{'quicksort', 'mergesort‘, 'heapsort', 'stable'}, 默认是quicksort
    order 排序字段

np.argsort(a, axis=-1, kind=None, order=None): 返回对数组进行排序索引。

** 在 numpy 中只要是 arg...()的方法, 返回的都是索引
"""
import numpy as np
from xarray.core.ops import argsort

a = np.array([
    [10, 3, 11],
    [7, 22, 15],
    [11, 15, 3]
])
b = np.sort(a, axis=0)
print(b)
c = np.sort(a, axis=1)
"""
[[ 3 10 11]
 [ 7 15 22]
 [ 3 11 15]]
"""
print(c)

d = argsort(a, axis=1)
"""
[[1 0 2]
 [0 2 1]
 [2 0 1]]
"""
print(d)