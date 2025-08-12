# arr_a = ['ethan', 'zoran', 'jim']
# 计算列表长度
# print(len(arr_a))

# # 列表中追加元素lucy
# arr_a.append('lucy')
# print(arr_a)

# 在列表中的第一个位置添加tony
# arr_a.insert(0, 'tony')
# print(arr_a)

# 修改第二个元素的字符为kelly
# arr_a[1] = 'kelly'
# print(arr_a)

# 删除列表中的ethan
# arr_a.remove('ethan')
# del arr_a[0]
# print(arr_a)

# 删除列表中的第二个元素
# arr_a.pop(1)
# print(arr_a)

# 给定一个列表nums = [10, 20, 30, 50, 70, 20]
# nums = [10, 20, 30, 50, 70, 20]
# 1.查询20首次出现索引位置，用遍历方式完成

#方案一:
# print(nums.index(20))

# 方案二:
# for idx, num in enumerate(nums):
#     if num == 20:
#         print(idx)
#         break

# 2.查询20出现的所有位置
# for idx, num in enumerate(nums):
#     if num == 20:
#         print(idx)

# 假设有一个列表names = ['曹操', '刘备', '关于', '张飞', '小乔', '诸葛亮']
# names = ['曹操', '刘备', '关于', '张飞', '小乔', '诸葛亮']

# 1.依次打印出所有人名
# for name in names:
#     print(name)

# 假设有一个列表names = [['张飞', '刘备', '关于'], ['曹操', '典韦', '司马懿']], 如何转化为
# ['张飞', '刘备', '关于', '曹操', '典韦', '司马懿']
# names = [['张飞', '刘备', '关于'], ['曹操', '典韦', '司马懿']]
#
# cl_names = []
# for item in names:
#     for name in item:
#         cl_names.append(name)
# print(cl_names)

# 现有1, 2, 3, 4四个数字, 求这个四个数字能组成多少个不重复的三位数

# 符合要求
# 1 2 3
# 3 2 1
# ...

# 不符合要求
# 1 2 2
# 1 1 2
# ...

nums = [1, 2, 3, 4]

# 第一个数有4种选择， 第二个数有3种选择， 第三个数有2种选择

"""
1
1 2 3
1 2 4
1 3 2
1 3 4
1 4 2
1 4 3

2
2 1 3
2 1 4
2 3 1
2 3 4
2 4 1
2 4 3


"""

for one in nums:
    print(one, 'one')
    for two in nums:
        if one != two:
            print(two, 'two')
        for three in nums:
            if three != one and three != two:
                print(three, 'three')


