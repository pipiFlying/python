"""
__new__(): 创建对象，给对象开辟内存空间
__init__(): 构造函数，给对象数据进行初始化
__str__(): 直接格式化对象或者输出对象的时候，返回当前对象的文本显示方式
__repr__(): 间接格式化对象或者输出对象的时候，返回当前对象的文本显示方式
当__str__函数没有被重写的时候，都会走__repr__
"""

# __str__() 和 __repr__(): 说明
class Pet:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

pet = Pet('胖子', 2)

print(pet) # <__main__.Pet object at 0x000001AEF3ECF680> 输出的这个字符串就是调用的__str__()


class Dog(Pet):

    def __str__(self) -> str:
        return 'Dog'

dog = Dog('旺财', 2)

print(dog) # Dog

class Cat(Pet):

    def __str__(self) -> str:
        return 'Cat'

cat = Cat('pipi', 2)

# 直接格式化
print(cat) # Cat
# 间接格式化
print([cat]) # [<__main__.Cat object at 0x000001764F9CFD40>]

class Pig(Pet):

    def __str__(self) -> str:
        return 'Pig'
    def __repr__(self) -> str:
        return 'Pig_A'

pig = Pig('pipi', 2)

# 直接格式化
print(pig) # Cat
# 间接格式化
print([pig]) # [Pig_A]

"""
== 默认比较的是地址值，但是python内置的数据类型都重写了 == 底层对应的魔术方法，变成比较内容

is 是关键字，比较的是地址值，不会被重写
"""

li_a = [1, 2, 3, 4]
li_b = [1, 2, 3, 4]
print(li_a == li_b) # True
print(li_a is li_b) # False

pig_a = Pig('pipi', 2)
pig_b = Pig('pipi', 2)
print(pig_a == pig_b) # False
print(pig_a is pig_b) # False

"""
__len__(): 当使用len()函数的时候其实底层调用的就是__len__()
__del__(): 当使用垃圾回收机制回收对象的时候调用的的就是__del__()
__getitem__(): 当使用索引访问元素的时候就是调用的__getitem__()
__setitem__(): 当使用索引给元素赋值的时候就是调用的__setitem__()
__delitem__(): 当使用索引删除元素的时候调用的__delitem__()
"""

"""
比较运算符对应的魔术方法：
    == 对应的魔术方法 __eq__()
    >  对应的魔术方法 __gt__()
    >= 对应的魔术方法 __ge__()
    <  对应的魔术方法 __lt__()
    <= 对应的魔术方法 __le__()
    != 对应的魔术方法 __ne__()
"""