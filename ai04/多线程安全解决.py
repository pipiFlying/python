"""
解决方案：锁对象threading.Lock
"""

import threading
import time

class WindowThread(threading.Thread):

    ticket = 10
    # 创建锁对象
    lock = threading.Lock()

    def run(self):
        while True:
            # 对共同访问数据处理逻辑加锁
            WindowThread.lock.acquire()
            if WindowThread.ticket > 0:
                print(f'{self.name}正在卖{WindowThread.ticket}张票')
                WindowThread.ticket -= 1
            # 释放锁
            WindowThread.lock.release()
            time.sleep(0.1)


if __name__ == '__main__':
    ta = WindowThread(name='窗口1')
    tb = WindowThread(name='窗口2')
    tc = WindowThread(name='窗口3')

    ta.start()
    tb.start()
    tc.start()