"""
random模块用于生成伪随机数
"""
import random

# 设置随机数种子，种子变化随机数就变化，种子数固定，随机数就固定
random.seed()

# randint(a, b): 返回[a, b]之间的随机数，左闭右闭
a = random.randint(1,8)
print(a, 'a')

# randrange 和 range函数使用方式一致，不同的是返回随机数
b = random.randrange(1, 8, 2)
print(b, 'b')

# random 返回的是[0, 1) 之间的浮点数
c = random.random()
print(c, 'c')

# uniform(a, b) 返回一个随机浮点数 N 当 a <= b 时 a <= N <= b，当 b < a 时 b <= N <= a
d = random.uniform(7, 4)
print(d, 'd')

# random.choice(seq) 从非空序列中返回一个随机元素，如果seq为空则引发IndexError
e = random.choice('abcdefgh')
print(e, 'e')

# random.choices(seq) 从非空序列中返回一k个随机元素，并组成列表返回，如果seq为空则引发IndexError
f = random.choices('abcdefgh', k=2)
print(f, 'f')

# shuffle() 随机打乱数据，修改的是原数据
li = [1, 2, 3, 4, 5]
random.shuffle(li)
print(li)

# sample(population, k, *, counts=None) 返回从总体序列中选取唯一元素长度为k的列表，用于无重复的随机数抽样
# counts: 表示每个元素可以被采样的次数，counts和population长度相同
# 无重复的随机数抽样，并非指数据不会重复，而是指抽过的数据不会再次放回再次抽取
li_a = [1, 2, 3, 4, 5, 5, 4, 6, 7, 2, 1]
g = random.sample(li_a, k=3)
print(g, 'g')

li_b = [1, 2, 3, 4, 5]
counts = [1, 2, 3, 1, 1] # 对应代表的是1可以抽样1次，2可以抽样2次，3可以抽样3次...
h = random.sample(li_b, k=5, counts=counts)
print(h, 'h')

