"""
使用随机数生成10个随机密码，密码要求是大小写字母和数字的组合，长度8位。提示：使用 string 模块

print(string.digits) # 0123456789
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
"""

import string, random

# 这样写出来的方法，可能出现全是数字，或者全是字母的密码
# def random_password(digit_number: int)->str:
#     tmp_strs = string.digits + string.ascii_letters
#     strs = ''
#     def put_str():
#         return random.choice(tmp_strs)
#     for i in range(digit_number):
#         strs += put_str()
#
#     return strs

def random_password(digit_number: int)->str:
    tmp_strs = string.digits + string.ascii_letters
    strs = ''
    def put_str():
        num_times = len([item for item in list(strs) if item in string.digits])
        letter_times = len([item for item in list(strs) if item in string.ascii_letters])
        if len(strs) >= 7:
            if not num_times:
                return random.choice(string.digits)
            elif not letter_times:
                return random.choice(string.ascii_letters)
            else:
                return random.choice(tmp_strs)
        else:
            return random.choice(tmp_strs)

    for i in range(digit_number):
        strs += put_str()

    return strs

if __name__ == '__main__':
    print(random_password(8))
