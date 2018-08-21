# -*- coding:UTF-8 -*-

'''
层序序列构造二叉树

思路：
参见

编程环境：
Python3.5.2

作者：
CSDN博客：https://my.csdn.net/yeqiang19910412
Github：https://github.com/YeQiang1075736553

日期：
2018.8.13
'''

class Node():
    """节点类"""
    def __init__(self,data=None,lchild=None,rchild=None):
        self.data = data  # 表示数据域
        self.lchild = lchild  # 表示左子树
        self.rchild = rchild  # 表示右子树

class BinaryTree():
    def __init__(self):
        self.root = None
        self.queue = []

    def add(self,data):
        """为树添加节点"""
        node = Node(data)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
            self.queue.append(self.root)
        else:
            tree_node = self.queue[0]
            if tree_node.lchild == None:
                tree_node.lchild = node
                self.queue.append(tree_node.lchild)
            else:
                tree_node.rchild = node
                self.queue.append(tree_node.rchild)
                self.queue.pop(0) # 如果该节点存在右孩子，则将队列中的第一个元素丢弃


    def pre_order_traverse(self,root):
        """递归实现前序遍历"""
        if root == None:
            return
        print(root.data,end=" ")
        self.pre_order_traverse(root.lchild)
        self.pre_order_traverse(root.rchild)

    def in_order_traverse(self,root):
        """递归实现后序遍历"""
        if root == None:
            return
        self.in_order_traverse(root.lchild)
        print(root.data,end=" ")
        self.in_order_traverse(root.rchild)

    def post_order_traverse(self,root):
        """递归实现后序遍历"""
        if root == None:
            return
        self.post_order_traverse(root.lchild)
        self.post_order_traverse(root.rchild)
        print(root.data,end=" ")

    def level_order_traverse(self,root):
        """队列实现层序遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.data,end=" ")
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

if __name__ == "__main__":
    #str = "abcd#ef#g##h#####"
    #str = "abcdefgh"
    str = "abc#d####"
    data = list(str)
    binary_tree = BinaryTree()
    for elem in data:
        binary_tree.add(elem)

    print("递归实现前序遍历")
    binary_tree.pre_order_traverse(binary_tree.root) # 递归实现前序遍历
    print("\n")
    print("递归实现中序遍历")
    binary_tree.in_order_traverse(binary_tree.root) # 递归实现中序遍历
    print("\n")
    print("递归实现后序遍历")
    binary_tree.post_order_traverse(binary_tree.root) # 递归实现后序遍历
    print("\n")
    print("队列实现层序遍历") # 队列实现层序遍历
    binary_tree.level_order_traverse(binary_tree.root)

