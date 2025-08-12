li01 = [('a', 3), ('b', 2), ('c', 1)]

def sort_key(item):
    return item[1]

# li01.sort(key=sort_key)

li01.sort(key=lambda item: item[1])

print(li01)

li02 = ['1', '3', '2']

li02.sort()

print(li02)

li03 = ['1', '101', '11']

li03.sort() # ['1', '101', '11']

print(li03)

# li03.sort(key=lambda item: int(item))
li03.sort(key=int)

print(li03)