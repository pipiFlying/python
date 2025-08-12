students = [
    {'name':'Tom', 'age':19, 'score':92, 'sex':'女','tel':'15300022839'},
    {'name':'Jerry', 'age':20, 'score':40, 'sex':'男','tel':'15300022838'},
]
# 遍历所有学生姓名
# for student in students:
#     print(student['name'])

# 统计不及格学生个数
# students_n = [student for student in students if student['score'] < 60]
# print(len(students_n))

# 打印所有男生的信息
# students_f = [student for student in students if student['sex'] == '男']
# print(students_f)

# 求平均分数
# total = 0
# for student in students:
#     total += student['score']
# print(total / len(students))