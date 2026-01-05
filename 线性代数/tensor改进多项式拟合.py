import random
import torch
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

_x = [ele / 100 for ele in range(100)]
_y = [3 * np.sin(5 * ele) + ele * 2 + 10 + random.random() for ele in _x]

_x = np.array(_x)
_y = np.array(_y)

# 定义模型
# y = w1 * x ** 5 + w2 * x ** 4 + w3 * x ** 3 + w4 * x ** 2 + w5 * x + w6

# 寻找叶子结点，x 是已知参数，调整的是w的值，所以w是叶子结点，要可导 requires_grad=True
# weights = torch.tensor([random.random() for _ in range(6)])

# 创建函数模型
def creat_model(x, order = 5):
    req = torch.tensor([x ** n for n in range(order, -1, -1)])
    print(req)
    return req

# 单点损失函数
def clac_loss(pred_y, true_y):
    err = pred_y - true_y
    return err ** 2

def train(epochs, learning_rate):
    weights = torch.tensor([random.random() for _ in range(6)], requires_grad=True, dtype=torch.float32)
    ax0 = plt.subplot(211)
    loss_list = []

    for epoch in range(epochs):
        for x, y in zip(_x, _y):
            powers = torch.tensor([x ** n for n in range(5, -1, -1)], dtype=torch.float32)
            pred_y = torch.dot(weights, powers)
            loss = clac_loss(pred_y, y)
            loss_list.append(loss)

            # 梯度清零
            if weights.grad is not None:
                weights.grad.data.zero_()

            # 计算梯度
            loss.backward()

            # 使用梯度更新参数
            weights.data -= learning_rate * weights.grad

        if epoch % 10 == 0:
            ax0.cla()
            ax0.scatter(_x, _y)
            ax0.plot(_x, [weights[0].item() * x ** 5 + weights[1].item() * x ** 4 + weights[2].item() * x ** 3 + weights[3].item() * x ** 2 + weights[4].item() * x + weights[5].item() for x in _x], color='red')
            ax0.set_title(f'epoch={epoch + 1}, loss={loss:.4f}, w1={weights[5].item():.4f}, w2={weights[4].item():.4f}, w3={weights[3].item():.4f}, w4={weights[2].item():.4f}, w5={weights[1].item():.4f}, w6={weights[0].item():.4f}')

            plt.pause(0.1)

    plt.show()

if __name__ == '__main__':
    train(10000, 0.1)
