i = 0
while i < 9:
    i += 1
    s = 0
    while s < i:
        s += 1
        if s == i:
            print(f'{s} * {i} = {s * i}', end='\n')
        else:
            print(f'{s} * {i} = {s * i}', end=' ')


