"""

python 中线程需要使用 threading 模块

创建线程的方式一：
    向构造器传一个可调用对象

1. 需要构造器，说明有类，这个类就是Thread
2. 传递一个可调用的对象，函数默认就是可调用对象
"""
import threading
import time
from threading import Thread

def play_music():
    for i in range(10):
        print('唱歌', threading.current_thread().name)
        time.sleep(1)

def play_dance():
    for i in range(10):
        print('跳舞', threading.current_thread().name)
        time.sleep(1)

# 阻塞式运行
# play_music()
# play_dance()

# 多线程同时进行
t_a = Thread(target=play_music)
# 启动线程
t_a.start()

t_b = Thread(target=play_dance)
# 启动线程
t_b.start()
