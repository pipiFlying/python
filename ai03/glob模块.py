"""
glob 模块会按照 Unix shell 所使用的规则查找出所有匹配特定模式的路径名称，返回结果的顺序是不确定的

glob 模块的作用：就是按照规则查找文件路径下的文件或文件夹

glob的规则：
    * 零个或多个字符 (.开头的文件不能匹配)
    ? 1个字符
    [abc] a或b或c
    [!a] 除了a以外的任意字符
    ** 是配合(递归)recursive=True的时候使用，用于递归查找
"""

import glob

list_a = glob.glob('E:/项目/python项目/ai03/*.py')
list_b = glob.glob('E:/项目/python项目/ai03/utils/test?r.yaml')
list_c = glob.glob('E:/项目/python项目/ai03/**/*', recursive=True) # 使用 ** 必须使用 recursive(递归) 否则仅匹配外层目录文件，不会逐层匹配
print(list_a)
print(list_b)
print(list_c)