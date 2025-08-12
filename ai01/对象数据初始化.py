# class Student:
#     name = '张三'
#     age = 18
#
# stu1 = Student()
# stu2 = Student()
#
# # 动态添加对象的属性，赋值即定义
# stu1.sex = '男'
# # . 语法，表示从属关系
# stu1.name = '王五'
# stu1.age = 20
# print(stu1.sex) # 男
#
# Student.name = '王麻子'
# print(stu2.name) # 王麻子

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self, '--> self')

stu1 = Student('杜甫', 30) # <__main__.Student object at 0x0000019673F0F410> --> self
stu2 = Student('李白', 20) # <__main__.Student object at 0x0000019673F0F440> --> self
print(stu1) # <__main__.Student object at 0x0000019673F0F410>
print(stu2) # <__main__.Student object at 0x0000019673F0F440>

"""
真实情况，赋值应该在__init__函数中进行，且每次实例化后的对象和对应该次__init__的self，self指向的就是该对象。

self 仅仅是一个参数名称，可以是任意标识符
"""