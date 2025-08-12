# 求 1! + 2! + 3! + 4! + 5! + 6! + ... + n!

"""
求 n!
"""

# def sum_s(n):
#     if n == 0 or n == 1:
#         return n
#     elif n < 0:
#         return NotImplemented # 未实现
#     else:
#         return n * sum_s(n-1)
#
# print(sum_s(5))

"""
求斐波那契数列的和

1 1 2 3 5 8 13 21 ...
"""
# 方案1
def ani(m):
    if m < 0:
        return NotImplemented
    elif m == 1 or m == 2:
        return 1
    else:
        return ani(m - 1) + ani(m - 2)

print(ani(8))
