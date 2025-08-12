"""
在使用 open 读取文件操作中，打开文件 --- 读取数据 --- 关闭资源
关闭资源是需要手动close完成，这种方式容易忘记，导致资源没有释放

此时with上下文，将操作文件的代码写在with上下文中，操作完成后会自动释放资源

with上下文没有作用域
"""
with open('test/a.txt', mode='rt', encoding='utf-8') as f:
    print(f.read())