score = input('请输入分数:')
int_score = int(score)

if int_score >= 90:
    print('A')
elif int_score >= 80:
    print('B')
elif int_score >= 70:
    print('C')
elif int_score >= 60:
    print('D')
elif int_score >= 50:
    print('E')
else:
    print('F')