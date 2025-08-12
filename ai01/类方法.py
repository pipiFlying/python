"""
类方法:
    使用@classmethod修饰的方法就是类方法

被@classmethod修饰的方法，无论是被
    类.函数名()
    还是
    实例对象.函数名()
都会被python解释器转成 绑定方法 bound method

且@classmethod的使用场景，工厂函数：

可以通过set_cat(cls, name, age):函数，直接创建实例对象，不通过__init__函数
"""

class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def eat(cls):
        print('吃鱼')

    @classmethod
    def set_cat(cls, name, age):
        return cls(name, age)

    def run(self):
        print(self.name, '爱跑步')


cat = Cat('狸花猫', 1)
print(cat.eat) # <bound method Cat.eat of <class '__main__.Cat'>>
print(Cat.eat) # <bound method Cat.eat of <class '__main__.Cat'>>

cat_b = Cat.set_cat('布偶猫', 2)
cat_b.run()