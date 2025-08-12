"""
可调用对象

*   就是可以直接在 对象名后面添加() 调用对应的功能
*   对象名()

python中函数就是可调用对象

可调用对象必须实现 __call__()魔术方法，才能成为可调用对象

"""
class Dog:

    def eat(self):
        print('啃骨头')

dog = Dog()
# dog() # TypeError: 'Dog' object is not callable

class Cat:

    def eat(self, meal):
        print('吃', meal)

    def __call__(self, *args, **kwargs):
        self.eat(args)

cat = Cat()
cat('大鲨鱼') # 吃 ('大鲨鱼',)