import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer

df = pd.read_csv('train.csv')
print(df)

# 获取Age数据
ages = df['Age']
print(ages)
# 通过Series得到ndarray
X = ages.values
print(X)
# 特征数据要求是二维，所以需要改变形状
X = X.reshape(-1, 1)

# 将Age的缺失值进行填充，默认使用均值填充
imputer = SimpleImputer(strategy='mean', missing_values=np.nan)
imputer.fit(X)
_age = imputer.transform(X)

# 将填充值更新df
df['Age'] = _age
print(df['Age'])