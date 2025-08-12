# def fn():
#     x = 10
#     def show():
#         x = 100
#         print(x)
#     show()
#
# fn()

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

print(counter()())