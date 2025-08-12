# 求解1-100中能被3整除的所有数字和
# total = 0
# i = 0
# while i <= 100:
#     i += 1
#     if i % 3 == 0:
#         total += i
# print(total)

#求解1-100中能被3和5同时整除的所有数字和
# total = 0
# i = 0
# while i <= 100:
#     i += 1
#     if i % 3 == 0 and i % 5 == 0:
#         total += i
# print(total)

#使用 while 完成以下图形输出
"""
*
**
***
****
"""
# i = 0
# while i < 4:
#     i += 1
#     print('*' * i)
"""
****
***
**
*
"""
# i = 5
# while i > 1:
#     i -= 1
#     print('*' * i)

# 求 1 + 1/2 + 1/3 + 1/4 + 1/5 的和
"""
1 + 2 + 3 + 4 + 5
—————————————————
1 * 2 * 3 * 4 * 5
"""
# sum_s = int(1) + float(1/2) + float(1/3) + float(1/4) + float(1/5)
# print(sum_s)

# 使用for循环完成九九乘法表
# row = 1
# for clo in range(row):
#     print(f'{clo + 1} * {row} = {(clo + 1) * row}', end=' ')
# print()
# row = 2
# for clo in range(row):
#     print(f'{clo + 1} * {row} = {(clo + 1) * row}', end=' ')
# print()
# row = 3
# for clo in range(row):
#     print(f'{clo + 1} * {row} = {(clo + 1) * row}', end=' ')
# print()
# row = 4
# for clo in range(row):
#     print(f'{clo + 1} * {row} = {(clo + 1) * row}', end=' ')
# print()
# 结果
# row = 10
# for j in range(row):
#     for clo in range(j):
#         print(f'{clo + 1} * {j} = {(clo + 1) * j}', end=' ')
#     print()

# 输入一个二进制数判断二进制数中1的个数
# in_value = input('请输入数字:')
# int_in_value = int(in_value)
# bin_value = bin(int_in_value)
# print(bin_value)
# k = 0
# for i in range(2, len(bin_value)):
#     if bin_value[i] == '1':
#         k += 1
# print(k)

# 输入1234, 返回4321
str_a = '1234'
str_b = ''
for i in range(len(str_a)):
    print(type(i))
    str_b += str_a[3-i]
print(str_b)
