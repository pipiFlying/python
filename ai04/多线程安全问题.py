"""
线程安全问题
    满足条件：
    1. 多个线程环境
    2. 访问共享数据
    3. 多个线程对共享数据进行修改

解决方案：锁对象threading.Lock
"""

import threading
import time

class WindowThread(threading.Thread):

    ticket = 10

    def run(self):
        while True:
            if WindowThread.ticket > 0:
                print(f'{self.name}正在卖{WindowThread.ticket}张票')
                WindowThread.ticket -= 1

            time.sleep(0.1)


if __name__ == '__main__':
    ta = WindowThread(name='窗口1')
    tb = WindowThread(name='窗口2')
    tc = WindowThread(name='窗口3')

    ta.start()
    tb.start()
    tc.start()