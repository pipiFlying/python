class Person:
    name = '张三'
    age = 20

    @staticmethod
    def eat():
        print('吃饭')


p1 = Person()
print(p1) # <__main__.Person object at 0x0000022856B0F680>
print(Person)  # <class '__main__.Person'>
print(Person.name) # 张三
print(Person.age) # 20
print(p1.name) # 张三
print(p1.age) # 20
p1.eat()