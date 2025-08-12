# 输入一个数找出在nums里面出现的所有位置
# nums = [10, 20, 30, 50, 20]
#
# def find_num_index_all(num, traget):
#     position = [idx for idx, item in enumerate(traget) if item == num]
#     return position
#
# print(find_num_index_all(20, nums))
# print(find_num_index_all(30, nums))

# 定义一个函数实现返回三个的和
# def calc_total(a, b, c):
#     if type(a) == (int or float) and type(b) == (int or float) and type(c) == (int or float):
#         return a + b + c
#     else:
#         print('请输入数字')
#
# print(calc_total('7', 2, 3))

# 定义一个函数获取三个数的最小值
# def get_min(x, y, z):
#     min_num = y if x > y else x
#     min_num = z if min_num > z else min_num
#     return min_num
#
# print(get_min(1, 2, 3))

# 定义一个函数求阶乘 n! = 1 * 2 * 3 * ... * n
# def get_num_n(n):
#     a = 1
#     for i in range(n):
#         a *= (i + 1)
#     return a
# print(get_num_n(4))

# 定义一个函数求阶乘 1 + 2! + 3! + 4! + ... + 20!
# def get_num_n_all(s):
#     total = 0
#     for i in range(s):
#         total += get_num_n(i + 1)
#     return total
#
# print(get_num_n_all(4))

# 前k个高频元素

nums = [2, 3, 1, 2, 3, 3, 3, 4, 4, 4]

def get_top_n(k):
    set_nums = set(nums)
    set_nums_li = list(set_nums)
    set_nums_li.sort(reverse=True)
    print(set_nums_li)
    arr = [{num: nums.count(num)} for num in set_nums_li]
    return arr[:k]
print(get_top_n(2))