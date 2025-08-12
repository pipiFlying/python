class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def look_door(self):
        print(self.name, '看门')

dog = Dog('皮皮', 2)

dog.look_door() # 用实例点，无需传参

print(dog.look_door) # <bound method Dog.look_door of <__main__.Dog object at 0x0000022608C03500>>

print(Dog.look_door) # <function Dog.look_door at 0x0000026279BBC680>

Dog.look_door(dog) # 用类点，需要传参

"""
look_door方法定义的时候是有参数self的，但是使用实例dog调用look_door并没有传参，代码没有报错
原因：对象.函数名()的时候，python解释器会将函数转成'绑定方法'，然后将调用的对象绑定给函数中的第一个参数self

绑定方法：
dog.look_door # <bound method Dog.look_door of <__main__.Dog object at 0x0000022608C03500>>
函数：所以需要传参
Dog.look_door # <function Dog.look_door at 0x0000026279BBC680>
"""