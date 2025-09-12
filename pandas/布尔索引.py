# import numpy as np
import numpy as np
import pandas as pd

data = np.array([11, 12, 13, 14, 15])
# data = [11, 12, 13, 14, 15]
s1 = pd.Series(data, index=[*'abcde'])
# 就是给Series设置名称
s1.name = '设置名称'
print(s1)
"""
a    11
d    14
dtype: int64
"""
print(s1[[True, False, False, True, False]])
"""
d    14
e    15
dtype: int64
"""
print(s1[s1 > 13])