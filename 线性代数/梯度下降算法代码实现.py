import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random

_x = [0.0, 0.20408163, 0.40816327, 0.6122449,  0.81632653, 1.02040816,
  1.2244898, 1.42857143, 1.63265306, 1.83673469, 2.04081633, 2.24489796,
  2.44897959, 2.65306122, 2.85714286, 3.06122449, 3.26530612, 3.46938776,
  3.67346939, 3.87755102, 4.08163265, 4.28571429, 4.48979592, 4.69387755,
  4.89795918, 5.10204082, 5.30612245, 5.51020408, 5.71428571, 5.91836735,
  6.12244898, 6.32653061, 6.53061224, 6.73469388, 6.93877551, 7.14285714,
  7.34693878, 7.55102041, 7.75510204, 7.95918367, 8.16326531, 8.36734694,
  8.57142857, 8.7755102,  8.97959184, 9.18367347, 9.3877551, 9.59183673,
  9.79591837, 10.0]

_x = np.array(_x)

_y = [6.03887625e+00, 2.59379182e-02, 4.13692381e+00, 3.10003370e+00,
 3.31566266e+00, 4.06356026e+00, 5.65802142e+00, 3.41817470e+00,
 8.89832416e+00, 8.53545393e+00, 8.40054894e+00, 8.08751192e+00,
 1.15618441e+01, 1.05351793e+01, 8.62416592e+00, 1.28114836e+01,
 1.54310530e+01, 1.49978181e+01, 9.80250113e+00, 1.16919089e+01,
 1.42343953e+01, 1.21595129e+01, 1.48882379e+01, 1.44430725e+01,
 1.82987777e+01, 1.62693276e+01, 1.61426521e+01, 1.65616364e+01,
 1.91208745e+01, 1.75068069e+01, 1.85871783e+01, 2.06064021e+01,
 1.96663597e+01, 1.96877905e+01, 1.82300249e+01, 2.28062593e+01,
 2.04418676e+01, 2.40161444e+01, 2.02396700e+01, 2.49425436e+01,
 2.35362424e+01, 2.53386094e+01, 2.52710697e+01, 2.50153250e+01,
 2.51403220e+01, 2.79149861e+01, 2.69393477e+01, 2.85503043e+01,
 2.44111177e+01, 2.86605056e+01]

_y = np.array(_y)

# 创建模型
# 根据数据图形显示得到该数据最匹配线性模型
# pre_y = w * x + b

# 创建模型
def creat_model(w, x, b):
    return w * x + b

# 确定损失函数
def mse_loss(pred_y, true_y):
    return np.mean((pred_y - true_y) ** 2)

# 使用mse对参数w和b进行求导
def get_grad(x, pred_y, true_y):
    error = pred_y - true_y
    grad_w = 2 * np.mean(error * x)
    grad_b  = 2 * np.mean(error)
    return grad_w, grad_b

def train(epochs, learn_rate):
    w = random.random()
    b = random.random()

    ax0 = plt.subplot(211)
    ax1 = plt.subplot(212)
    loss_list = []

    for epoch in range(epochs):
        pred_y = creat_model(w, _x, b)
        # 使用预测值和真实值比较计算损失
        loss = mse_loss(pred_y, _y)
        loss_list.append(loss)
        # 使用mse对w和b进行求导，得到梯度
        grad_w, grad_b = get_grad(_x, pred_y, _y)
        # 使用梯度更新参数
        w -= learn_rate * grad_w
        b -= learn_rate * grad_b

        ax0.cla()
        ax0.scatter(_x, _y)
        ax0.plot(_x, pred_y, color='red')
        ax0.set_title(f'epoch={epoch + 1}, loss={loss:.4f}, w={w:.4f}, b={b:.4f}')

        ax1.cla()
        ax1.plot(loss_list, color='red')
        ax1.set_xlabel('epoch')
        ax1.set_ylabel('loss')

        plt.pause(0.01)
        if (epoch + 1) % 10 == 0:
            print(f'epoch {epoch + 1}: loss={loss:.4f}, w={w:.4f}, b={b:.4f}')

    plt.show()
    return w, b

if __name__ == '__main__':
    train(1000, 0.01)

