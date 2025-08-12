a = 5  # 0000 0101
b = 8

f = 3 # 0000 0011

c = 5 >> 2
g = f >> 2

print(c)
print(g)

arr = [1,2,3,4]

if f in arr:
    print('True ' + 'f in arr')

if b not in arr:
    print('True ' + 'b not in arr')

ft = '50'
fb = '50'

if ft is fb:
    print('True ' + 'ft is fb')

if id(ft) == id(fb):
    print('True ' + 'id(ft) == id(fb)')

if ft is not fb:
    print('True ' + 'ft is not fb')
else: print('False ' + 'ft is not fb')

if (kf := 5) < 8:
    print(kf)
    print('True ' + 'kf := 5 < 8')

fs = 10
fd = 20

print(fs and fd)
print(fs or fd)
# print('\a')

def check_status(status):
    match status:
        case 200:
            return 'success'
        case 401:
            return 'denied'
        case 500:
            return 'failed'
        case _:
            return 'unknown'

print(check_status(200))

sums = 0
count = 0
while count < 10:
    print(count)
    sums += count
    count += 1

print(sums)

lists = ['a', 'b', 'c']
for item in lists:
    print(item)

for i in range(len(lists)):
    print(i, lists[i])

