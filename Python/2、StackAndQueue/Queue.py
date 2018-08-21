# -*- coding:UTF-8 -*-

'''
队列（Queue）

思路：
参见 https://blog.csdn.net/yeqiang19910412/article/details/81192791

编程环境：
Python3.5.2

作者：
CSDN博客：https://my.csdn.net/yeqiang19910412
Github：https://github.com/YeQiang1075736553

日期：
2018.8.13
'''

# 定义一个队列类
class Queue():
    # 队列初始化
    def __init__(self):
        self.items = []

    # 判断队列是否为空,为空返回True
    def is_empty(self):
        return self.items == []

    # 进队列
    def en_queue(self,data):
        self.items.insert(0,data)

    # 出队列
    def de_queue(self):
        return self.items.pop()

    # 判断队列的大小
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.en_queue("hello")
    q.en_queue("world")
    q.en_queue("itcast")
    print(q.size())
    print(q.de_queue())
    print(q.de_queue())
    print(q.de_queue())
