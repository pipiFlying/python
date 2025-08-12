class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if self.age < 0:
            self.age = 18

p_a = Person('李白', -32)
print(vars(p_a)) # {'name': '李白', 'age': 18}
p_a.age = -11
print(vars(p_a)) # {'name': '李白', 'age': -11}
"""
age 虽然在__init__函数中被做了限制，但是 p_a.age 赋值方式确不受限制
"""

"""
改进为如下的方式，pa_a.__age = -11 无法修改 Persona 类里面的age
"""
class Persona:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        if self.__age < 0:
            self.__age = 18

pa_a = Persona('杜甫', -32)
print(vars(pa_a)) # {'name': '杜甫', '_Persona__age': 18}
pa_a.__age = -11
print(vars(pa_a)) # {'name': '杜甫', '_Persona__age': 18, '__age': -11}