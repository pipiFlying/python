import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

_x = [ele / 100 for ele in range(100)]
_y = [3 * np.sin(5 * ele) + ele * 2 + 10 + random.random() for ele in _x]

_x = np.array(_x)
_y = np.array(_y)

# 创建函数模型
def creat_model(w1, w2, w3, w4, w5, w6, x):
    return w1 * x ** 5 + w2 + x ** 4 + w3 * x ** 3 + w4 * x ** 2 + w5 * x + w6

# 计算损失
def clac_loss(pred_y, true_y):
    err = pred_y - true_y
    return err ** 2
# 计算梯度
def clac_grad(pred_y, true_y):
    return 2 * (pred_y - true_y)

def train(epochs, learning_rate):
    w1 = random.random()
    w2 = random.random()
    w3 = random.random()
    w4 = random.random()
    w5 = random.random()
    w6 = random.random()
    ax0 = plt.subplot(211)
    loss_list = []

    for epoch in range(epochs):
        for x, y in zip(_x, _y):
            pred_y = creat_model(w1, w2, w3, w4, w5, w6, x)
            loss = clac_loss(pred_y, y)
            loss_list.append(loss)
            grad = clac_grad(pred_y, y)

            # 计算梯队对w的导数
            grad_w1 = grad * x ** 5
            grad_w2 = grad * x ** 4
            grad_w3 = grad * x ** 3
            grad_w4 = grad * x ** 2
            grad_w5 = grad * x
            grad_w6 = grad

            # 使用梯度更新参数
            w1 -= learning_rate * grad_w1
            w2 -= learning_rate * grad_w2
            w3 -= learning_rate * grad_w3
            w4 -= learning_rate * grad_w4
            w5 -= learning_rate * grad_w5
            w6 -= learning_rate * grad_w6

        if epoch % 10 == 0:
            ax0.cla()
            ax0.scatter(_x, _y)
            ax0.plot(_x, [creat_model(w1, w2, w3, w4, w5, w6, x) for x in _x], color='red')
            ax0.set_title(f'epoch={epoch + 1}, loss={loss:.4f}, w1={w1:.4f}, w2={w2:.4f}, w3={w3:.4f}, w4={w4:.4f}, w5={w5:.4f}, w6={w6:.4f}')

            plt.pause(0.1)

    plt.show()


if __name__ == '__main__':
    train(10000, 0.1)
