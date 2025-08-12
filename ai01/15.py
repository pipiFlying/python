arr_a = ['tom', 'jim', 'tim']
# 末尾添加
arr_a.append('som') # ['tom', 'jim', 'tim', 'som']
print(arr_a)
# 下表插入
arr_a.insert(2, 'rom') # ['tom', 'jim', 'rom', 'tim', 'som']
print(arr_a)
arr_a.remove('tom') # ['jim', 'rom', 'tim', 'som']
print(arr_a)
arr_b = ['pipi', 'wen']
arr_a.extend(arr_b ) # ['jim', 'rom', 'tim', 'som', 'pipi', 'wen']
print(arr_a)
arr_c = [7, 9, 8, 6]
arr_c.sort()
print(arr_c)
arr_c.sort(reverse=True)
print(arr_c)