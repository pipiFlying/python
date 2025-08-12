def out(a, b):
    print(a, b)

t1 = (1, 2)
out(*t1)

t2 = 20, 30
out(*t2)

t3 = [40, 50]
out(*t3)

t4 = 'xy'
out(*t4)

t5 = {'a': 1, 'b': 2}
out(*t5)
out(**t5)

t6 = {'name': '张三', 'age': 20}
# out(*t6)
out(**t6)