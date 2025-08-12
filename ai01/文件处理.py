"""
路径path: 就是用来定位资源
    计算机中路径分为:
        绝对路径: 直接使用路径就能访问到资源
            常见'E:\项目\python项目\ai01\异常处理.py'或'https://www.baidu.com'
        弊端：移植性较差，换了环境可能访问不了

        相对路径: 必须借助参照路径，才能定位资源
            参照路径: 当前文件所在路径

os.listdir()

"""
import os

# os.mkdir(path): 创建一个名为path的文件夹
# os.mkdir('test')

# os.mkdir(path): 创建多级目录
# os.makedirs('test/a')

# os.rmdir(path): 删除空目录, 如果目录不存在，就引发FileNotFoundError 或 OSError
# os.rmdir('b')

# os.removedirs(path): 递归删除空目录，path 需指向最里面一层路径，会从里面逐层向外递归删除目录
# os.removedirs('test')

# os.remove(path) 删除文件
# os.remove('a.txt')

"""

os.path.exists(path) 判断文件是否存在

需要先判断判断文件或目录是否存在，否则以下两个，即便是相关类型，但是文件或目录不存在也会返回False
    os.path.isfile(path) 判断path是现有常规文件，则返回 True
    os.path.isdir(path) 如果path是现有目录，则返回 True

os.path.join(path, *path) 拼接多个路径

"""

"""
os.listdir(path) 返回当前路径下的内容组成的列表
"""

# files = os.listdir('E:\项目/python项目/ai01/')
# print(files)
