# -*- coding:UTF-8 -*-

'''
单向链表（SingleLinkedlist）

思路：
参见 https://blog.csdn.net/yeqiang19910412/article/details/80881250

编程环境：
Python3.5.2

作者：
CSDN博客：https://my.csdn.net/yeqiang19910412
Github：https://github.com/YeQiang1075736553

日期：
2018.8.13
'''

class Node():
    """单链表的节点"""
    def __init__(self,data):
        # self._data存放数据域
        self._data = data
        # self._next存放下一个节点的地址
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,new_data):
        self._data = new_data

    def set_next(self,new_next):
        self._next = new_next

class SingleLinkedList():
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空：判断头结点的指针域是否为空"""
        return self._head == None

    def length(self):
        """链表长度：遍历链表，不为空长度就加一"""
        # curr_node 初始时指向头结点
        curr_node = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while curr_node != None:
            count += 1
            # 将当前节点curr_node后移一个节点
            curr_node = curr_node.get_next()
        return count

    def travel(self):
        """遍历链表"""
        curr_node = self._head
        while curr_node != None:
            print(curr_node.get_data())
            curr_node = curr_node.get_next()

    def add(self,data):
        """头部添加节点"""
        # step1:先创建一个保存data值的新节点
        new_node = Node(data)
        # step2:将新节点的指针域next指向头结点，即self._head指向的位置
        new_node.set_next(self._head)
        # step3:将链表的头节点self._head指向新节点
        self._head = new_node

    def append(self,data):
        """尾部添加节点"""
        # step1:先创建一个保存data值的新节点
        new_node = Node(data)
        # step2:先判断链表是否为空，若是空链表，则将self._head指向新节点
        if self.is_empty():
            self._head = new_node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            curr_node = self._head
            while curr_node.get_next() != None:
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)

    def insert(self,pos,data):
        """指定位置后添加节点"""
        # 若指定位置pos为第一个节点之前，则执行头部插入
        if pos <= 0:
            self.add(data)
        # 若指定位置pos超过链表尾部，则执行尾部插入
        elif pos>= self.length():
            self.append(data)
        #  找到指定位置
        else:
            new_node = Node(data)
            count  = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头结点开始移动到指定的位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.get_next()
            # 现将新节点new_node的next指向插入位置的节点
            new_node.set_next(pre.get_next())
            # 将插入位置的前一个节点的next指向新节点
            pre.set_next(new_node)

    def remove(self,data):
        """删除第一个匹配的节点"""
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        curr_node = self._head
        pre = None
        # 若头结点的元素就是要查找的元素data
        if curr_node.get_data() == data:
            # 如果链表不止一个节点
            if curr_node.get_next() != None:
                # 将self._head指向第二个节点
                self._head = curr_node.get_next()
            else:
                # 链表只有一个节点
                self._head = None
        # 若头结点的元素不是要查找的元素data
        else:
            while curr_node != None:
                # 找到了要删除的数据
                if curr_node.get_data() == data:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.set_next(curr_node.get_next())
                    break
                # 没有找到了要删除的数据，继续按链表向后移动节点
                else:
                    # 继续按链表向后移动节点
                    pre = curr_node
                    curr_node = curr_node.get_next()

            # 要删除的元素不存在
            if curr_node == None:
                print("NO %d element" % data)

    def search(self,data):
        """链表查找节点是否存在，并返回Ture或者False"""
        if self.is_empty():
            return False
        curr_node = self._head
        while curr_node != None:
            if curr_node.get_data() == data:
                return True
            curr_node = curr_node.get_next()
        return False

if __name__ == "__main__":
    ll = SingleLinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.append(4)
    ll.insert(-1,5) # 插入位置小于0
    ll.insert(10,5) #插入位置大于链表长度
    ll.insert(2,5)
    ll.remove(3) # 移除头结点
    ll.remove(4) # 移除尾节点
    ll.remove(5) # 移除中间节点
    ll.remove(10) # 移除不存在节点
    ll.travel()
    print(ll.search(3))
    print(ll.search(22))
    print(ll.is_empty())
    print(ll.length())





