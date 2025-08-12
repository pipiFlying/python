"""
使用sorted函数实现字典排序，要求使用lamada的方式完成
- 按照key排序
- 按照value排序
"""

# 按照key排序
# nums = {'1': 3, '3': 2, '2': 1, '4': 4}
#
# li01 = sorted(nums.items(), lambda x: int(x[0]))
#
# print(dict(li01))

# 按照value排序
# nums = {'1': 3, '3': 2, '2': 1, '4': 4}
#
# li01 = sorted(nums.items(), key=lambda x: x[1])
#
# print(dict(li01))

"""
使用lamada和三目运算符实现两个数据a,b比大小，谁大返回谁

思考
def ab_max(a, b):
    return a if a > b else b

lambda a, b: a if a > b else b
"""

max_a = lambda a, b: a if a > b else b

print(max_a(3, 2))

"""
实现一个数二进制的函数
"""
bin(10)
print(f'{10: 08b}') # 08就是补位数


