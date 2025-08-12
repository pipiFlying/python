class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('吃东西')

# 需要新增 color 属性
class Cat(Pet):
    def __init__(self, name, age, color):
        # 语法1
        # super().__init__(name, age)
        # 语法2
        super(Cat, self).__init__(name, age)
        self.color = color

    def catch_mouse(self):
        print('抓老鼠')
    # 直接覆盖父类方法
    def eat(self):
        print('猫吃鱼')

cat = Cat('布偶猫', 2, '黄白')

print(vars(cat)) # {'name': '布偶猫', 'age': 2, 'color': '黄白'}

cat.eat()