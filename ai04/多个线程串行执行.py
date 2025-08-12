"""
串行：顺序执行

join(): 加入线程
    作用：在哪一个线程中调用join()，哪一个线程就会阻塞，直到线程a 执行完成

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

ta = Thread(target=play_music)

tb = Thread(target=play_dance)

ta.start()
"""
ta.join() 在mainThread中调用的，所以mainThrea被阻塞，
直到ta执行完成，mainThread才能解除阻塞继续执行

ta.join(timeout) 参数，提供最大阻塞时间。

    如果阻塞时间过长，主线程执行完毕后，后面的线程也会执行
"""
ta.join()
tb.start()