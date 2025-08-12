class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('吃东西')

class Dog:
    def eat(self):
        print('啃骨头')

class Cat:
    def eat(self):
        print('吃鱼')

class Person:
    def feed(self, pet):
        pet.eat()

p = Person()
p.feed(Dog()) # 啃骨头
p.feed(Cat()) # 吃鱼