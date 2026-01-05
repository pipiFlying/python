import torch

image = torch.tensor([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])

kernel = torch.tensor([[1, 0], 
                       [0, -1]])

# 得到image宽高
h, w = image.shape
kh, kw = kernel.shape

_container = torch.empty(h - kh + 1, w - kw + 1)

print(h, w, kh, kw)

for row in range(h - 1):
    for col in range(w -1):
        print(row, col, image[row:row+2, col:col+2])
        # dot 只能计算一维 flatten() 降维成一维列表
        dot_result = torch.dot(image[row:row+2, col:col+2].flatten(), kernel.flatten())
        print(dot_result)
        _container[row:row+2, col:col+2] = dot_result

print(_container)

s = torch.tensor([[[1, 2, 3, 4]]])

print(s.flatten())
