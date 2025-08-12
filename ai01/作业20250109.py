"""
使用面向对象实现以下程序

************欢迎进入真术平台************
1，添加用户名
2，显示指定用户
3，修改指定用户
4，删除指定用户
5，显示所有用户
请输入选择编号
要求：
根据选择的不同编号，实现对应功能
用户输入用户名只能是数字或字母组合，长度3-8位，否则提示用户非法
"""
import re

class Card:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Zs:
    def __init__(self):
        self.cards = []

    def add(self, card):
        if isinstance(card, Card):
            self.cards.append(card)

    def show_user(self, name):
        for card in self.cards:
            if card.name == name:
                print(f'name: {card.name}, age: {card.age}')
                return card
            else:
                print('查无此人')

    def update_user(self, name, new_name, new_age):
        for card in self.cards:
            if card.name == name:
                card.name = new_name
                card.age = new_age

    def del_user(self, name):
        for card in self.cards:
            if card.name == name:
                self.cards.remove(card)
                print('删除成功')

    def show_all_user(self):
        for card in self.cards:
            print(f'name: {card.name}, age: {card.age}')

    def have_user(self, name):
        for card in self.cards:
            if card.name == name:
                return True
        return False

def verify(name):
    if re.match('[a-zA-Z0-9]{3,8}$', name):
        return True
    else:
        return False

def screen():
    print('欢迎进入真术平台'.center(30, '*'))
    print('1. 添加用户名', '2. 显示指定用户', '3. 修改指定用户', '4. 删除指定用户', '5. 显示所有用户', sep='\n')

def actions(key):
    match key:
        case '1':
            name = input('请输入姓名:')
            while not verify(name):
                print('用户名非法，用户名只能是数字或字母组合，长度3-8位')
                name = input('请输入姓名:')
            age = input('请输入年龄:')
            zs.add(Card(name, age))
        case '2':
            name = input('请输入要显示的指定用户姓名:')
            zs.show_user(name)
        case '3':
            name = input('请输入要修改的指定用户姓名:')
            if not zs.have_user(name):
                print('查无此人')
                return
            else:
                new_name = input('请输入新的用户姓名:')
                if not new_name:
                    new_name = zs.show_user(name).name
                else:
                    while not verify(new_name):
                        print('用户名非法，用户名只能是数字或字母组合，长度3-8位')
                        new_name = input('请输入新的用户姓名:')
                new_age = input('请输入新的年龄:')
                if not new_age:
                    new_age = zs.show_user(name).age
                zs.update_user(name, new_name, new_age)
        case '4':
            name = input('请输入要删除的指定用户姓名:')
            if zs.have_user(name):
                zs.del_user(name)
        case '5':
            zs.show_all_user()
        case _:
            print('请输入正确的提示信息！')

zs = Zs()
while True:
    screen()
    enter_key = input('请输入:')
    actions(enter_key)

