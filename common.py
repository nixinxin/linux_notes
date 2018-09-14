import socket

def shuru():
    sk1 = socket.socket()
    sk1.connect(("localhost", 1234))
    while True:
        # content1 = str(sk1.recv(1024), encoding="utf-8")
        a = []
        # print(content1)
        inp = "1234"
        if inp == "q":
            a.append(inp)
            break
        else:
            sk1.sendall(bytes(inp, encoding="utf-8"))
            content2 = str(sk1.recv(1024), encoding="utf-8")
            print(content2)
            inp = "q"
        if a == ["q"]:
            break
    sk1.close()


# !/usr/bin/env python
# -*- coding;utf-8 -*-
"""
    自定义线程池博客园教程地址
        http://www.cnblogs.com/wupeiqi/articles/4839959.html
"""
import queue
import threading
import time


class ThreadPool(object):

    def __init__(self, max_num=100):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)

    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)


def func(arg):
    shuru()
    # 在队列中增加线程类


if __name__ == "__main__":
    # 在队列中创建线程类
    pool = ThreadPool(1000)
    for i in range(1000):
        # 获得类
        thread = pool.get_thread()
        # 对象 = 类（）
        ret = thread(target=func, args=(pool,))
        ret.start()