# -*- coding:UTF-8 -*-

'''
前序遍历创建二叉树

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
    def __init__(self,data_list):
        """初始化传入的列表为迭代器"""
        self.iter = iter(data_list)

    def pre_order_create(self,root=None):
        """前序遍历创建二叉树"""
        try:
            # 获取下一个元素
            next_data = next(self.iter)
            # 如果next_data为"#"，则判断为到达扩展二叉树的叶子节点
            if next_data == "#":
                root = None
            else:
                root = Node(next_data)
                root.lchild = self.pre_order_create(root.lchild)
                root.rchild = self.pre_order_create(root.rchild)
        except Exception as e:
            print(e)
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
    str = "abd#g###ce##fh###"
    data = list(str)
    binary_tree = BinaryTree(data)
    root = binary_tree.pre_order_create()
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