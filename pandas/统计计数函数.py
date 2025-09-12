"""
sum(): 求和
cumsum(): 累计总和
mean(): 平均值
max() 和 idxmax(): 分别找出最大值及其索引位置
min() 和 idxmin(): 分别找出最小值及其索引位置
describe(): 提供一个包含计数、平均值、标准差、最小值、四分位数和最大值的统计摘要
"""
import numpy as np
import pandas as pd

data = np.arange(1, 7).reshape(2, 3)
df1 = pd.DataFrame(data)
"""
   0  1  2
0  1  2  3
1  4  5  6
"""
print(df1)

# 默认0轴
# df1.sum(axis=0)
s = df1.sum()
print(s)
