# score = int(input('请输入分数：'))
#
# def is_pass(score):
#     return '及格' if score >= 60 else '不及格'
#
# print(is_pass(score))

def get_min(x, y, z):
    min_num = y if x > y else x
    min_num = z if min_num > z else min_num
    return min_num

print(get_min(1, 2, 3))