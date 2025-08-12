def gen():
	yield 10
	yield 11
	yield 12
	yield 13
	yield 14

g = gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
