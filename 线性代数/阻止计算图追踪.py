import torch

t = torch.arange(1, 13).reshape(3, 4)
print(t)

# is_contiguous(): 判断张量在内存中是否连续
# 连续的话查询效率高
print(t.is_contiguous())

# 切片操作会将张量变成不连续的张量
y = t[:, 0:2]
print(y)
print(y.is_contiguous())

# 将你不连续的张量变成连续的张量
z = y.contiguous()
print(z)
print(z.is_contiguous())