"""
1.编程实现：投100轮骰子，每轮3次，统计出每轮连续出现6点次数
x 6 6
6 6 x
6 6 6
"""
# import random
#
# def run_dice(total_times: int, loop_times: int):
#     times = []
#     def run_loop(k):
#         arr = []
#         for i in range(loop_times):
#             ran_num = random.randint(1, 6)
#             arr.append(ran_num)
#         match arr:
#             case [x, 6, 6] | [6, 6, x] if x != 6:
#                 times.append({f'第{k}轮': 1})
#                 # times.append(1)
#             case [6, 6, 6]:
#                 times.append({f'第{k}轮': 2})
#                 # times.append(2)
#             case _:
#                 times.append({f'第{k}轮': 0})
#                 # times.append(0)
#     for j in range(total_times):
#         run_loop(j)
#     return times
#
# calc_res = run_dice(100, 3)
# print(calc_res)

"""
- 封装Student类，包含属性name、age、tel、score、sex、
  包含方法getScore(打印name、score)
  getStudent(打印个人全部信息)

- 使用list对象，存储5个学生对象，迭代所有学生信息

- 打印出不及格学生信息及统计不及格学生数量
"""

class Student:
    def __init__(self, name: str, age: int, tel: str, score: float, sex: str):
        self.name = name
        self.age = age
        self.tel = tel
        self.score = score
        self.sex = sex

    def get_score(self):
        print('name:', self.name, 'score:', self.score)

    def get_student(self):
        print('name:', self.name, 'age:', self.age, 'tel:', self.tel, 'score:', self.score, 'sex:', self.sex)

stu_a = Student('李白', 20, '13177564521', 90, '男')
stu_b = Student('杜甫', 25, '13177564522', 88, '男')
stu_c = Student('李清照', 23, '13177564523', 82, '女')
stu_d = Student('苏轼', 33, '13177564524', 80, '男')
stu_e = Student('花园宝宝', 33, '13177564525', 55, '男')

list_a = [
    {'name': stu_a.name, 'age': stu_a.age, 'tel': stu_a.tel, 'score': stu_a.score, 'sex': stu_a.sex},
    {'name': stu_b.name, 'age': stu_b.age, 'tel': stu_b.tel, 'score': stu_b.score, 'sex': stu_b.sex},
    {'name': stu_c.name, 'age': stu_c.age, 'tel': stu_c.tel, 'score': stu_c.score, 'sex': stu_c.sex},
    {'name': stu_d.name, 'age': stu_d.age, 'tel': stu_d.tel, 'score': stu_d.score, 'sex': stu_d.sex},
    {'name': stu_e.name, 'age': stu_e.age, 'tel': stu_e.tel, 'score': stu_e.score, 'sex': stu_e.sex},
]

print(list_a)

total_p = 0

for item in list_a:
    print(item)
    if item['score'] < 60:
        total_p += 1

print(total_p)

