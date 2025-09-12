"""
read_csv()
read_excel()
read_table()
"""
import numpy as np
import pandas as pd

df1 = pd.read_csv('a.csv')
"""
     id name  age
0  1001   张三   20
1  1002   李四   32
"""
print(df1)

df2 = pd.read_csv('a.csv', names=['name','age'])
"""
      name  age
id    name  age
1001    张三   20
1002    李四   32
"""
print(df2)
"""
name    张三
age     20
Name: 1001, dtype: object
"""
print(df2.loc['1001'])

# 将数据中的id作为行索引
df3 = pd.read_csv('a.csv', index_col='id')
"""
     name  age
id            
1001   张三   20
1002   李四   32
"""
print(df3)
"""
name    张三
age     20
Name: 1001, dtype: object
"""
print(df3.loc[1001])

# index_col 起到的作用和重命名DataFrame命名行索引相似
data2 = np.arange(1, 13).reshape(3, 4)
df4 = pd.DataFrame(data=data2)
df4.index.name = 'id'
"""
    0   1   2   3
id               
0   1   2   3   4
1   5   6   7   8
2   9  10  11  12
"""
print(df4)
