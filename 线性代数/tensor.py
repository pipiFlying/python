import torch
import numpy as np

# 创建tensor
t1 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], device='cuda:0')
print(t1)

# numpy转tensor
t2 = np.arange(1, 10).reshape(3, 3)
t2 = torch.from_numpy(t2)
print(t2)

t3 = torch.zeros(3, 3)
print(t3)
t4 = torch.zeros_like(t1)
print(t4)
print(t4.dtype)