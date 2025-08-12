"""
程序中的非致命异常都继承自 Exceptoion 即可

Exceptoion 包含错误类型， 但是不建议直接用 Exceptoion 而使用详细错误类

Error: 语法错误
Exceptoion: 程序解析没有问题，但是程序执行的过程中可能遇到问题

捕获异常：
- 找到可能出现异常的代码
- 将改代码使用
    try:
        ...
    except Exceptoion as e:
        print('出现异常', e)

    except 可以有多个

try 中发生异常后的代码也不会执行

finally: 常用于资源释放

try ... except 语句中具有可选的 else 语句，该语句必须放在所有except之后
该语句适用于 try 没有引发错误捕获，但是又必须执行的代码
"""

try:
    a = 9 / 0
    print('next') # try 中发生异常语句后的代码也不会执行
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except (ValueError, IndexError) as e:
    print(e)
except OverflowError as e:
    print(e)
finally:
    print('finally')


"""
手动触发异常 raise

"""
def factorial(n):
    if n < 0:
        raise ValueError('n must be positive')
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

factorial(-1)