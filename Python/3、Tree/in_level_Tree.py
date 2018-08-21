# -*- coding:UTF-8 -*-

'''
中序序列和层序序列构造二叉树

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
        pass

    def in_level_construct_tree(self,mid_order,level_order):
        """根据中序序列和层序序列构造二叉树"""
        if len(mid_order)==0 or len(level_order)==0:
            return None
        # 层序遍历的第一个结点一定是根结点
        root_data = level_order[0]
        root = Node(root_data)
        i = mid_order.index(root_data)

        Lin = mid_order[:i] # 利用层序遍历确定的根节点划分出左右子树
        Rin = mid_order[i+1:]

        Llevel = []
        Rlevel = []
        for i in range(len(level_order)): # 通过中序序列，找到层序序列中相同的左右子树元素，并按顺序排列
            for j in range(len(Lin)):
                if level_order[i] == Lin[j]:
                   Llevel.append(level_order[i])
        for i in range(len(level_order)):
            for j in range(len(Rin)):
                if level_order[i] == Rin[j]:
                   Rlevel.append(level_order[i])

        root.lchild = self.in_level_construct_tree(Lin,Llevel)
        root.rchild = self.in_level_construct_tree(Rin,Rlevel)

        return root

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

    def level_order_traverse(self, root):
        """队列实现层序遍历"""
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

if __name__ == '__main__':
    str_mid = "dgbaechf"
    str_level = "abcdefgh"
    mid_order = list(str_mid)
    level_order = list(str_level)
    binary_tree = BinaryTree()
    root = binary_tree.in_level_construct_tree(mid_order,level_order)
    print("递归实现前序遍历")
    binary_tree.pre_order_traverse(root) # 递归实现前序遍历
    print("\n")
    print("递归实现中序遍历")
    binary_tree.in_order_traverse(root) # 递归实现中序遍历
    print("\n")
    print("递归实现后序遍历")
    binary_tree.post_order_traverse(root) # 递归实现后序遍历
    print("\n")
    print("队列实现层序遍历") # 队列实现层序遍历
    binary_tree.level_order_traverse(root)


