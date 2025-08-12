"""
1. 程序启动，提示用户登录或者注册
2. 选择注册-> 要求用户输入用户名和密码->将用户名和密码保存到文件中->返回注册提示信息
3. 选择登录->要求输入用户名和密码->判断是否登录成功

json.load() 加载空的 json 文件时会报错，且json.load()读取的就是字符串，将字符转格式json转化成真正的json文件
所以初始写入文件时直接使用
f.write('[]') 或者 f.write('{}') 即可
"""
import os
import json

class Database:

    @staticmethod
    def creat_database():
        have_database = os.path.isdir('database')
        if not have_database:
            os.mkdir('database')
            with open('database/user.json', 'w', encoding='utf-8') as database:
                database.write('[]')

    @staticmethod
    def add_user(user_name, psw):
        with open('database/user.json', 'r+', encoding='utf-8') as r_f:
            datas = json.load(r_f)
            datas.append({ 'user_name': user_name, 'psw': psw })

        with open('database/user.json', 'w+', encoding='utf-8') as w_f:
            json.dump(datas, w_f, indent=4)

    @staticmethod
    def get_user(user_name):
        with open('database/user.json', 'r', encoding='utf-8') as database:
            datas = json.load(database)
            for user in datas:
                if user_name == user['user_name']:
                    return user

    @staticmethod
    def have_user(user_name):
        with open('database/user.json', 'r', encoding='utf-8') as database:
            datas = json.load(database)
        for user in datas:
            if user_name == user['user_name']:
                return True
        return False

    @staticmethod
    def verify_user(user_name, psw):
        with open('database/user.json', 'r+', encoding='utf-8') as r_f:
            datas = json.load(r_f)
            for user in datas:
                if user_name == user['user_name'] and psw == user['psw']:
                    return True
            return False

def screen():
    print('欢迎登录宇宙人系统'.center(30, '*'))
    print('1. 注册', '2. 登录', sep='\n')

def actions(enter_key):
    match enter_key:
        case '1':
            register()
        case '2':
            login()
        case _:
            print('请根据提示，输入正确命令!')

def register():
    user_name = input('请输入用户名: ')
    print(Database.have_user(user_name), 'Database.have_user(user_name)')
    if Database.have_user(user_name):
        print('用户已完成注册，请登录')
    else:
        psw = input('请输入密码: ')
        Database.add_user(user_name, psw)
        print('用户注册成功')

def login():
    user_name = input('请输入用户名: ')
    if not Database.have_user(user_name):
        print('用户未注册, 请注册！')
    else:
        psw = input('请输入密码: ')
        print('登录成功') if Database.verify_user(user_name, psw) else print('密码错误！')

def init():
    while True:
        screen()
        key = input('请选择: ')
        actions(key)

# Database.creat_database()
init()


"""
定义函数，实现任意文件复制
"""
def copy_file(or_path: str, tr_path: str)->None:
    with open(or_path, mode='rb') as f_or:
        file = f_or.read()
        with open(tr_path, mode='wb') as f_tr:
            f_tr.write(file)

"""
将一下数据写入文件
"""
# 定义数据
data = [
    ['path', 'x', 'y', 'w', 'h'],
    ['1.png', '100', '100', '200', '200'],
    ['2.png', '50', '100', '100', '100'],
    ['3.png', '200', '50', '150', '100'],
    ['4.png', '150', '100', '100', '100']
]

with open('test/gs.txt', 'w', encoding='utf-8') as gs_f:
    for item in data:
        for children in item:
            gs_f.write(children + '\t')
        gs_f.write('\n')
