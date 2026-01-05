import numpy as np
# StandardScaler 标准化处理模块
from sklearn.preprocessing import StandardScaler

# x` = (x - 特征数据均值) / 特征数据标准差

X = np.array([[1, 8, 20], [888, 2, 10]])

# 标准化处理
scaler = StandardScaler()
# 调用fit
scaler.fit(X)
print(scaler.mean_)
print(scaler.var_)
# 调用transform
y = scaler.transform(X)
print(y)
# 获取标准化后的均值
print(y.mean())
# 获取标准化后的方差
print(y.var())