# 完全导入
# import utils
#
# print(utils.nums)
#
# sums = utils.add(3, 4)
# print(sums)

# 别名导入
# import utils as uta
#
# print(uta.nums)
#
# sums = uta.add(3, 4)
# print(sums)

# 部分导入
# from utils import nums, add
#
# print(nums)
#
# sums = add(3, 4)
# print(sums)

# 使用 * 导入模块内容
# 如果定义了__all__,那么使用 * 导入的时候 导入的就是__all__中定义的内容
from utils import *

print(nums)

sums = add(3, 4)
print(sums)