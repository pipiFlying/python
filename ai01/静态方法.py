class Cat:

    def __init__(self):
        pass

    @staticmethod
    def eat():
        print('吃鱼')

    def sleep(self):
        print('睡觉')

    @staticmethod
    def run(addr):
        print(f'在{addr}里跑')

print(Cat.eat()) # 吃鱼
# print(Cat.sleep()) # TypeError: Cat.sleep() missing 1 required positional argument: 'self'
Cat.run('家')
"""
普通方法和静态方法比较：
    1.普通方法使用时，必须先创建实例对象才能使用，因为必须要有实例对象传入给self
    2.静态方法使用时，无需创建实例对象即可使用，因为有了类静态方法就可以使用
    3.静态方法也是可以传值的，但是不会将第一个参数当做传入的对象
"""

cat = Cat()

print(cat.eat) # <function Cat.eat at 0x000001DFD58AC680>
print(Cat.eat) # <function Cat.eat at 0x000001DFD58AC680>

"""
使用@staticmethod修饰的函数，在对象.函数名()调用的情况下，就不会被python解释器转成'绑定函数'，而就是普通函数
"""
print(Cat.eat) # <function Cat.eat at 0x000001DFD58AC680>
