"""
写数据的时候，是先将数据写入缓冲区，然后再将缓冲区的数据写入文件

什么时候缓冲区数据会写入文件
    - 缓冲区数据满了
    - 手动将缓冲区数据刷写入文件 f.flush()
"""

# with open('test/a.txt', mode='at', encoding='utf-8') as f:
#
#     f.write('\n追加文字\n')

"""
复制文件，temp.txt 内容复制到 past.txt
"""

# with open('test/temp.txt', mode='rt', encoding='utf-8') as fa:
#     words = fa.read()
#     print(words)
#
# with open('test/past.txt', mode='w+t', encoding='utf-8') as fb:
#     fb.write(words)
#     fb.seek(0)
#     fg = fb.read()
#     print(fg)

def copy_file(or_path: str, tr_path: str)->None:
    with open(or_path, mode='rb') as f_or:
        file = f_or.read()
        with open(tr_path, mode='wb') as f_tr:
            f_tr.write(file)

copy_file('test/temp.txt', 'test/past.txt')

copy_file('test/testb/fd.txt', 'test/testb/temp.txt')

copy_file('test/testb/temp-img.jpeg', 'test/testb/past-img.jpeg')