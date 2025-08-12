"""
1. 实现一个班级点名器，要求：
    a. 学生信息储存在json文件中’
    b. 点名要实现随机出现名字
    c. 连续两次出现的名字不能相同
"""
import json
import random

last_id = None

def class_get_student(path):
    with open(path, 'r', encoding='utf-8') as fr:
        data = json.load(fr)

    def random_id():
        global last_id
        if type(data) is list:
            idxs = list(range(len(data)))
            filter_idxs = [i for i in idxs if i != last_id]
            r_id = random.choice(filter_idxs)
            last_id = r_id
            return data[r_id]

    return random_id()

if __name__ == '__main__':
    while True:
        i = input('按下开始随机抽取：')
        out_student = class_get_student('../zuoye/students.json')
        print(out_student)
