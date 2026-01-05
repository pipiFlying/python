"""
KNN: 作用实现分类
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

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

# 计算欧氏距离
euclidean_distance = np.linalg.norm(data - pred_data, axis=1)
# 对距离进行从小到大排序，得到index即可
euclidean_distance_index = np.argsort(euclidean_distance)
# 截取前K个数据进行预测
euclidean_distance_index_K = euclidean_distance_index[:K] # [1 6 3]
# 找到这截取的K个数据，对应的 labels 特征
K_labels = labels[euclidean_distance_index_K] # [0 1 0]
# 再对特征进行计数，谁多则预测值就是什么特征
# ndarray 众数获取
unique, counts = np.unique(K_labels, return_counts=True)
# 得出结论是0，那么预测值就是0
mode = unique[np.argmax(counts)] # 0

plt.show()