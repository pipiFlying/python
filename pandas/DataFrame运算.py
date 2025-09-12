"""
算术运算
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

# 加法运算 df.add() 逐元素相加
df1_1 = df1.add(3)
"""
    0   1   2   3
0   4   5   6   7
1   8   9  10  11
2  12  13  14  15
"""
print(df1_1)

# 形状相同对应元素相加
df1_2 = df1.add(df1)
"""
    0   1   2   3
0   2   4   6   8
1  10  12  14  16
2  18  20  22  24
"""
print(df1_2)