import torch.nn as nn
import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torch import optim
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class LeNet5(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            # 输入层 (N, 1, 32, 32)
            # 因为训练 minist 数据是 28 * 28
            # 改造(N, 1, 32, 32) -> (N, 1, 28, 28)
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, padding='same'),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=6, out_channels=6, kernel_size=5, padding='same'),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5),
            nn.ReLU(inplace=True),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5),
            nn.ReLU(inplace=True),
            # (N, C, H, W) -> (N, V)
            nn.Flatten(),
            nn.Linear(in_features=120, out_features=84),
            nn.ReLU(inplace=True),
            nn.Linear(in_features=84, out_features=10)
        )

    def forward(self, data):
        return self.layer(data)

if __name__ == '__main__':
    # 训练集
    batch_size = 100
    data_sets = datasets.MNIST(root='./data', train=True, transform=transforms.ToTensor(), download=True)
    data_loader = DataLoader(dataset=data_sets, batch_size=batch_size, shuffle=True)

    # 测试集
    test_sets = datasets.MNIST(root='./data', train=False, transform=transforms.ToTensor(), download=True)
    test_loader = DataLoader(dataset=test_sets, batch_size=batch_size)

    # 创建对象
    net = LeNet5().to(device)
    # 训练次数
    epochs = 100
    # 创建损失函数
    loss_fn = nn.CrossEntropyLoss(reduction='sum')
    # 创建优化器
    optimizer = optim.Adam(net.parameters(), lr=0.001)
    X, Y = [], []
    for epoch in range(epochs):
        # 明确设置为训练模式
        net.train()
        total_loss = 0
        for images, labels in data_loader:
            images, labels = images.to(device), labels.to(device)
            logits = net(images)
            loss = loss_fn(logits, labels)
            total_loss += loss
            # 梯度清零
            optimizer.zero_grad()
            # 反向传播
            loss.backward()
            # 更新参数
            optimizer.step()

        avg_loss = total_loss / len(data_sets)
        print(f'epoch: {epoch}, train_loss: {avg_loss}')
        # 定义测试总损失
        test_total_loss = 0
        # 进入评估模式
        net.eval()
        # 每轮训练完成，进行一次测试验证
        with torch.no_grad():
            correct = 0
            for test_images, test_labels in test_loader:
                test_images, test_labels = test_images.to(device), test_labels.to(device)
                test_logits = net(test_images)
                test_loss = loss_fn(test_logits, test_labels)
                test_total_loss += test_loss
                # print(test_labels) tensor([7, 2, 1, 0, 4, 1, 4, 9, 5, 9, 0, 6, 9, 0, 1, 5, 9, 7, 3, 4, 9, 6, 6, 5,
                #         4, 0, 7, 4, 0, 1, 3, 1, 3, 4, 7, 2, 7, 1, 2, 1, 1, 7, 4, 2, 3, 5, 1, 2,
                #         4, 4, 6, 3, 5, 5, 6, 0, 4, 1, 9, 5, 7, 8, 9, 3, 7, 4, 6, 4, 3, 0, 7, 0,
                #         2, 9, 1, 7, 3, 2, 9, 7, 7, 6, 2, 7, 8, 4, 7, 3, 6, 1, 3, 6, 9, 3, 1, 4,
                #         1, 7, 6, 9], device='cuda:0')
                # 计算模型预测正确样本数
                pred = torch.argmax(test_logits, dim=-1)
                # print(pred)        tensor([7, 2, 1, 0, 4, 1, 4, 9, 5, 9, 0, 6, 9, 0, 1, 5, 9, 7, 8, 4, 9, 6, 6, 5,
                #         4, 0, 7, 4, 0, 1, 3, 1, 3, 4, 7, 2, 7, 1, 2, 1, 1, 7, 4, 2, 3, 5, 1, 2,
                #         4, 4, 6, 3, 5, 5, 6, 0, 4, 1, 9, 5, 7, 8, 9, 3, 7, 4, 6, 4, 3, 0, 7, 0,
                #         2, 9, 1, 7, 3, 2, 9, 7, 7, 6, 2, 7, 8, 4, 7, 3, 6, 1, 3, 6, 9, 3, 1, 4,
                #         1, 7, 6, 9], device='cuda:0')
                # 计算预测正确的样本个数
                # 使用pred和test_labels进行逐元素比较，得到结果True表示预测准确，False表示预测错误
                # True表示1，False表示0，所以最终计算True的个数也就是1的和，就是预测正确的个数
                correct += torch.sum(pred == test_labels)

            # 每轮测试完成后输出测试样本的平均损失
            test_avg_loss = test_total_loss / len(test_sets)

            # 每轮测试完成后计算准确率
            success = correct * 100 / len(test_sets)
            print(f'test_loss: {test_avg_loss}, 准确率: {success}%')

    #     X.append(epoch)
    #     Y.append(total_loss.item())
    #     plt.cla()
    #     plt.plot(X, Y)
    #     plt.pause(0.1)
    # plt.show()
    # 训练结束后保存模型
    torch.save(net.state_dict(), 'lenet5_mnist.pth')
    print("Model saved as 'lenet5_mnist.pth'")
