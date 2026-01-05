

import numpy as np
from sklearn.preprocessing import MinMaxScaler

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 对X进行归一化，默认将特征数据归一化到0~1
scaler = MinMaxScaler()
# 调用fit函数
scaler.fit(X)
print('--------------')
print(scaler.data_max_)
print(scaler.data_min_)
print('--------------')
# 调用transform
y = scaler.transform(X)

# 两者步骤合一
z = scaler.fit_transform(X)

print(y)
print(z)

