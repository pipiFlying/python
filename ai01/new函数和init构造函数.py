class Student:
    name = '张三'
    age = 18

    # def __new__(cls, *args, **kwargs):
    #     print('__new__')

    def __init__(self, name, age):
        print(name, age)

stu = Student('王五', 20)
print(stu)