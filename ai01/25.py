li01 = [11, 23, 14, 25, 30]
li_m = filter(lambda a: a % 2 == 0, li01)

print([item for item in li_m])

li_x = map(lambda a: a - 10, li01)

print([item for item in li_x])

for item in li_x:
    print(item)

li02 = ['a', 'b', 'c']
li03 = [1, 2, 3]

zip_ob = zip(li02, li03)

print([item for item in zip_ob])