"""
KNN: 作用实现分类
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.neighbors import KNeighborsClassifier
matplotlib.use('TkAgg')

# 样本数据
data = np.array([
    [1.8, 2.9],
    [2.8, 4.9],
    [3.2, 2],
    [1, 5],
    [5.8, 8],
    [6.2, 4],
    [1.9, 5.9],
    [5, 5.6],
    [4.2, 7],
    [2.7, 6],
])
# 待预测值
pred_data = np.array([[2, 5]])
# 拟合范围
K = 3
# 对样本的特征标记
labels = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

data_0 = data[labels == 0]
data_1 = data[labels == 1]

plt.scatter(data_0[:, 0], data_0[:, 1], color='red', marker='o')
plt.scatter(data_1[:, 0], data_1[:, 1], color='blue', marker='^')
plt.scatter(pred_data[:, 0], pred_data[:, 1], color='green', marker='x')

# 创建对象
knn_classifier = KNeighborsClassifier(n_neighbors=K)
knn_classifier.fit(data, labels)
pred_label = knn_classifier.predict(pred_data) # 0

plt.show()