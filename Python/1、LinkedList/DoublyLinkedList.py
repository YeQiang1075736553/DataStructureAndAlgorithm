# -*- coding:UTF-8 -*-

'''
双向链表（DoublyLinkedList）

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
        self._prev = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def get_prev(self):
        return self._prev

    def set_data(self,new_data):
        self._data = new_data

    def set_next(self,new_next):
        self._next = new_next

    def set_prev(self,new_prev):
        self._prev = new_prev


class DoublyLinkedList():
    """双向链表"""
    def __init__(self):
        self._head  = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """返回链表的长度"""
        curr_node = self._head
        count = 0
        while curr_node != None:
            count += 1
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
        new_node = Node(data)
        # 如果是空链表，将self._head指向新节点
        if self.is_empty():
            self._head = new_node
        else:
            # 将new_node的next指向self._head的头结点
            new_node.set_next(self._head)
            # 将self._head的头结点的prev指向new_node
            self._head.set_prev(new_node)
            # 将self._head指向new_node
            self._head = new_node

    def append(self,data):
        """尾部添加节点"""
        new_node = Node(data)
        if self.is_empty():
            # 如果是空链表，将self._head指向new_node
            self._head = new_node
        else:
            # 移到链表尾部
            curr_node = self._head
            while curr_node.get_next() != None:
                curr_node = curr_node.get_next()
            # 将尾节点curr_node的next指向new_node
            curr_node.set_next(new_node)
            # 将new_node的prev指向curr_node
            new_node.set_prev(curr_node)

    def insert(self,pos,data):
        """指定位置后添加节点"""
        if pos<=0:
            self.add(data)
        elif pos>=self.length():
            self.append(data)
        else:
            new_node = Node(data)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头结点开始移动到指定的位置
            pre = self._head

            while count < pos-1:
                count += 1
                pre = pre.get_next()
            # 将new_node的prev指向pre
            new_node.set_prev(pre)
            # 将new_node的next指向pre的下一个节点
            new_node.set_next(pre.get_next())
            # 将pre的下一个节点的prev指向new_node
            pre.get_next().set_prev(new_node)
            # 将pre的next指向node
            pre.set_next(new_node)

    def remove(self,data):
        """删除第一个匹配的节点"""
        if self.is_empty():
            return
        curr_node = self._head
        # 若头结点的元素就是要查找的元素data
        if curr_node.get_data() == data:
            # 如果链表不止一个节点
            if curr_node.get_next() != None:
                # 将第二个节点的prev设置为None
                curr_node.get_next().set_prev(None)
                # 将self._head指向第二个节点
                self._head = curr_node.get_next()
            else:
                # 链表只有一个节点
                self._head = None
        # 若头结点的元素不是要查找的元素data
        else:
            while curr_node != None:
                if curr_node.get_next() != None:
                    # 找到了要删除的数据
                    if curr_node.get_data() == data:
                        # 将curr_node的前一个节点的next指向curr_node的后一个节点
                        curr_node.get_prev().set_next(curr_node.get_next())
                        # 将curr_node的后一个节点的prev指向curr_node的前一个节点
                        curr_node.get_next().set_prev(curr_node.get_prev())
                        break
                    # 没有找到了要删除的数据，继续按链表向后移动节点
                    else:
                        curr_node = curr_node.get_next()
                else:
                    if curr_node.get_data() == data:
                        # 将curr_node的前一个节点的next指向curr_node的后一个节点
                        curr_node.get_prev().set_next(curr_node.get_next())
                        curr_node = curr_node.get_next()
                        break
                    else:
                        # 要删除的元素不存在
                        print("NO %d element" % data)
                        break

    def search(self,data):
        """查找元素是否存在"""
        curr_node = self._head
        while curr_node != None:
            if curr_node.get_data() == data:
                return True
            curr_node = curr_node.get_next()
        return False

if __name__ == "__main__":
    ll = DoublyLinkedList()
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