class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('吃东西')

class Dog(Pet):

    def look_door(self):
        print('看门')

class Cat():

    def catch_mouse(self):
        print('抓老鼠')