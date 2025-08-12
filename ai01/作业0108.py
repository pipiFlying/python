from toolz.curried import peekn

from utils import random_password

print(random_password(8), '工具使用')

"""
自定义容器, 具备以下功能：
a. 可以使用索引操作
b. 具备增删改查的功能
c. 打印容器对象的时候输出元素内容
"""

class Container:
    def __init__(self):
        self.__arr = []

    def __getitem__(self, index):
        return self.__arr[index]

    def __setitem__(self, index, value):
        self.__arr[index] = value

    def __delitem__(self, index):
        del self.__arr[index]

    def __str__(self):
        return str(self.__arr)

    def __len__(self):
        return len(self.__arr)

    # 如果不重写这个迭代器魔术方法，for 循环迭代默认走的是__getitem__通过取下标的方法
    def __iter__(self):
        return iter(self.__arr)

    def append(self, item):
        self.__arr.append(item)

    def remove(self, item):
        self.__arr.remove(item)

    def index(self, item):
        return self.__arr.index(item)

c = Container()
c.append(1)
c.append(2)
c.append(3)
c.append(4)
print(c)
print(c[1])
c[1] = 3
print(c)
c.remove(3)
print(c)
print(len(c))

for i in c:
    print(i)



