# -*- coding:UTF-8 -*-

'''
栈（Stack）

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

# 定义一个栈类
class Stack():
    # 栈的初始化
    def __init__(self):
        self.items = []

    # 判断栈是否为空,为空返回True
    def is_empty(self):
        return self.items == []

    # 向栈内压入一个元素
    def push(self,data):
        self.items.append(data)

    # 从栈内推出最后一个元素
    def pop(self):
        return self.items.pop()

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items)-1]

    # 判断栈的大小
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())