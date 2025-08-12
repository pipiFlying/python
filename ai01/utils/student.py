"""
自定义一个Student学生类，创建5个学生在容器中，完成增删改查
"""
from container import Container

class Student:

    def __init__(self, name, age, id_card, sex):
        self.name = name
        self.age = age
        self.id_card = id_card
        self.sex = sex

    def __repr__(self):
        return f'name:{self.name} age:{self.age} id_card:{self.id_card} sex:{self.sex}'

c = Container()

s_a = Student('李白', 25, 201501, '男')
s_b = Student('杜甫', 25, 201501, '男')
s_c = Student('李清照', 25, 201501, '女')
s_d = Student('苏轼', 25, 201501, '男')
s_e = Student('王维', 25, 201501, '男')

c.append(s_a)
c.append(s_b)
c.append(s_c)
c.append(s_d)
c.append(s_e)
print(c)
c[0].name = '欧阳询'
del c[0]
print(c)
print(c[0])

