"""
创建线程方式二：
    1. 子类继承Thread
    2. 重写run方法
"""

import threading

class MyThread(threading.Thread):

    def run(self):
        for i in range(10):
            print('do something', self.name, i)

ta = MyThread(name='子线程a')
ta.start()