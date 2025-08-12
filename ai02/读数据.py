# f = open('test/a.txt', mode='r+t', encoding='utf-8')
#
# print(f.read())
# f.close()

"""
f.read(size)

可用于读取文件内容，
    size 是可选参数，省略size或size为负数时，读取并返回整个文件内容
    size 去其他值时，读取并返回最多 size 字符(文本模式)或size字节(二进制模式)
    如已到达文本末尾时，f.read()返回空字符串('')
    
什么样的文件读写数据时候才能使用 text 格式呢？
    只要使用window自带的记事本打开文件，数据不乱码就可以使用t格式
"""

# fa = open('test/b.docx', mode='r+b')
# print(fa.read())

"""
f.readline()
从文件读取单行数据，默认以 \n 结束

f.close() 释放资源
"""
# fb = open('test/a.txt', mode='r+t', encoding='utf-8')
#
# while True:
#     line = fb.readline()
#     print(line, end='')
#     if not line:
#         break
#
# fb.close()

fc = open('test/a.txt', mode='r+t', encoding='utf-8')

for line in fc:
    print(line, end='')

fc.close()

