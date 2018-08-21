# -*- coding:UTF-8 -*-

'''
前序序列和中序序列构造二叉树

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

    def pre_in_construct_tree(self,pre_order, mid_order):
        """根据前序序列和中序序列构造二叉树"""
        if len(pre_order)==0 or len(mid_order)==0:
            return None
        # 前序遍历的第一个结点一定是根结点
        root_data = pre_order[0]
        root = Node(root_data)
        # for i in range(0,len(mid_order)):
        #     if root_data == mid_order[i]:
        #         break
        i = mid_order.index(root_data) #上面for循环替代
        # 递归构造左子树和右子树
        root.lchild = self.pre_in_construct_tree(pre_order[1:1+i],mid_order[:i])
        root.rchild = self.pre_in_construct_tree(pre_order[1+i:],mid_order[i+1:])
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
    str_pre = "abdgcefh"
    str_mid = "dgbaechf"
    pre_order = list(str_pre)
    mid_order = list(str_mid)
    binary_tree = BinaryTree()
    root = binary_tree.pre_in_construct_tree(pre_order, mid_order)
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


