# -*- coding:UTF-8 -*-

'''
单向循环链表（SingleCyclicLinkedlist）

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
    """节点"""
    def __init__(self,data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self,new_data):
        self._data = new_data

    def set_next(self,new_next):
        self._next = new_next


class SingleCyclicLinkedList():
    """单向循环链表"""
    def __init__(self):
        self._head  = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        # 如果链表为空，返回长度为0
        if self.is_empty():
            return 0
        count = 1
        curr_node = self._head
        while curr_node.get_next() != self._head:
            count += 1
            curr_node = curr_node.get_next()
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            print("empty SingleCyclicLinkedList!")
        curr_node = self._head
        print(curr_node.get_data())
        while curr_node.get_next() != self._head:
            curr_node = curr_node.get_next()
            print(curr_node.get_data())

    def add(self,data):
        """头部添加节点"""
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            new_node.set_next(self._head)
        # 添加的节点指向self._head
        else:
            new_node.set_next(self._head)
            # 移到链表尾部，将尾节点的next指向new_nede
            curr_node = self._head
            while curr_node.get_next() != self._head:
                curr_node = curr_node.get_next()
            curr_node.set_next(new_node)
            # self._head指向new_node
            self._head = new_node

    def append(self,data):
        """尾部添加节点"""
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            new_node.set_next(self._head)
        else:
            # 移到链表尾部
            curr_node = self._head
            while curr_node.get_next() != self._head:
                curr_node = curr_node.get_next()
            # 将尾节点指向node
            curr_node.set_next(new_node)
            # 将node指向头结点self._head
            new_node.set_next(self._head)

    def insert(self,pos,data):
        """在指定位置后添加节点"""
        if pos <= 0:
            self.add(data)
        elif pos >= self.length():
            self.append(data)
        else:
            new_node = Node(data)
            count = 0
            pre = self._head
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头结点开始移动到指定的位置
            while count < pos-1:
                count += 1
                pre  = pre.get_next()
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
        # 若头结点的元素就是要查找的元素data
        if curr_node.get_data() == data:
            # 如果链表不止一个节点
            if curr_node.get_next() != self._head:
                # 先找到尾节点，将尾节点的next指向第二个节点
                while curr_node.get_next() != self._head:
                    curr_node = curr_node.get_next()
                 # curr_node指向了尾节点
                curr_node.set_next(self._head.get_next())
                self._head = self._head.get_next()
            else:
                # 链表只有一个节点
                self._head = None
        # 若头结点的元素不是要查找的元素data
        else:
            pre = self._head
            while curr_node.get_next() != self._head:
                # 找到了要删除的数据
                if curr_node.get_data() == data:
                    pre.set_next(curr_node.get_next())
                    return
                else:
                    pre = curr_node
                    curr_node = curr_node.get_next()

            # curr_node指向了尾节点
            if curr_node.get_data() == data:
                pre.set_next(curr_node.get_next())
            else:
                # 要删除的元素不存在
                print("NO %d element"% data)

    def search(self,data):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        curr_node = self._head
        if curr_node == data:
            return True
        while curr_node.get_next() != self._head:
            curr_node = curr_node.get_next()
            if curr_node.get_data() == data:
                return True
        return False

if __name__ == "__main__":
    ll = SingleCyclicLinkedList()
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




