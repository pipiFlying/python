# 将可能使用OpenMP的库放在一起导入
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


class PLM(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer01 = nn.Linear(1, 80)
        self.layer02 = nn.Linear(80, 60)
        self.layer03 = nn.Linear(60, 40)
        self.layer04 = nn.Linear(40, 20)
        self.layer05 = nn.Linear(20, 1)
        self.relu = nn.ReLU()

    def forward(self, data):
        data = self.relu(self.layer01(data))
        data = self.relu(self.layer02(data))
        data = self.relu(self.layer03(data))
        data = self.relu(self.layer04(data))
        out = self.layer05(data)
        return out

if __name__ == '__main__':
    # 固定随机种子数
    np.random.seed(10)
    # 样本数量， X形状:(100, 1)
    # 1表示特征数量
    X = np.random.rand(100, 1) * 10
    # 样本数据，Y就是真实值
    Y = np.sin(X) + 0.1 * np.random.randn(100, 1)
    # 将numpy数组转成Tensor
    # float32 是因为 X 要和 W 进行加权求和 W 是浮点数
    x_tensor = torch.tensor(X, dtype=torch.float32)
    y_tensor = torch.tensor(Y, dtype=torch.float32)
    # 测试数据，当模型训练完成后，使用该数据进行测试
    # 如果测试数据和样本真实数据很接近，说明模型训练完成

    x_test = torch.FloatTensor(np.linspace(0, 10, 100)).reshape(-1, 1)

    # 训练模型
    epoches = 10000
    # 学习率
    learning_rate = 0.1
    # 创建模型对象
    net = PLM()
    # 创建损失函数
    mse_loss = nn.MSELoss()

    for epoch in range(epoches):
        # 使用模型进行前向传播
        pred_y = net(x_tensor)
        # 使用预测值和真实值计算损失
        loss = mse_loss(pred_y, y_tensor)
        # 梯度清零
        net.zero_grad()
        # 使用loss进行反向传播，计算梯度
        loss.backward()
        # 使用梯度更新参数：w和b
        # 所有参数都在net中
        for param in net.parameters():
            param.data -= learning_rate * param.grad

    # 循环完成，模型就训练完成，也就是说net是训练好的模型，也就是net中w和b已经训练处结果
    with torch.no_grad():
        y_test = net(x_test)

    # 绘制可视化效果图

    plt.scatter(x_tensor.detach().numpy(), y_tensor.detach().numpy())
    plt.scatter(x_test, y_test, color='red')
    plt.show()