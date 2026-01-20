import torch.nn as nn
from torchvision import datasets, transforms
import tqdm
import torch
from torch.utils.data import Dataset, DataLoader
from torch import optim
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class CNN(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            # 定义结构
            # 卷积 - 卷积 - 池化 - 卷积 - 卷积 - 全连接神经网络
            # (N, C, H, W) - (N, 1, 28, 28) -> (N, 10, 26, 26)
            nn.Conv2d(1, 10, kernel_size=3),
            nn.ReLU(inplace=True),
            # (N, 10, 26, 26) -> (N, 6, 24, 24)
            nn.Conv2d(10, 6, kernel_size=3),
            nn.ReLU(inplace=True),
            # (N, 6, 24, 24) -> (N, 6, 12, 12)
            nn.MaxPool2d(2, 2),
            # (N, 6, 12, 12) -> (N, 4, 10, 10)
            nn.Conv2d(6, 4, kernel_size=3),
            nn.ReLU(inplace=True),
            # (N, 4, 12, 12) -> (N, 4, 8, 8)
            nn.Conv2d(4, 4, kernel_size=3),
            nn.ReLU(inplace=True),

            # 建立全连接层 -- 十分类
            # (N, C, H, W) -- (N, V)
            # 将(C, H, W) 展平成 V
            nn.Flatten(),
            nn.Linear(4 * 8 * 8, 128),
            nn.ReLU(inplace=True),
            nn.Linear(128, 32),
            nn.ReLU(inplace=True),
            nn.Linear(32, 10)
        )

    def forward(self, data):
        out = self.layer(data)
        return out

if __name__ == '__main__':
    # 创建数据集
    dataset = datasets.MNIST('data', train=True, download=True, transform=transforms.ToTensor())
    # 加载数据
    data_loader = DataLoader(dataset, batch_size=100, shuffle=True)
    # 创建模型
    net = CNN()
    # 选择设备训练
    net.to(device)
    # 训练轮次
    epoches = 1000
    # 创建损失函数
    loss_fn = nn.CrossEntropyLoss()
    # 创建优化器
    optimizer = optim.Adam(net.parameters(), lr=0.001)
    X = []
    Y = []
    for epoch in tqdm.tqdm(range(epoches)):
        train_total_loss = 0
        for images, labels in data_loader:
            # 选择设备训练
            images, labels = images.to(device), labels.to(device)
            logits = net(images)
            loss = loss_fn(logits, labels)
            train_total_loss += loss
            # 梯度清零
            optimizer.zero_grad()
            loss.backward()
            # 更新参数
            optimizer.step()

        # 每轮训练后计算样本总损失
        avg_train_loss = train_total_loss / len(data_loader)
        print(f'epoch: {epoch}, train_loss: {avg_train_loss}')
        X.append(epoch)
        Y.append(avg_train_loss.item())
        plt.cla()
        plt.plot(X, Y)
        plt.pause(0.1)
    plt.show()