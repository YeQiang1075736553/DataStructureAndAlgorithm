# -*- coding:UTF-8 -*-

'''
求树的深度

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
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data  # 表示数据域
        self.lchild = lchild  # 表示左子树
        self.rchild = rchild  # 表示右子树

class BinaryTree():
    def __init__(self, data_list):
        """初始化传入的列表为迭代器"""
        self.iter = iter(data_list)

    def pre_order_create(self, root=None):
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

    def tree_depth(self, root):
        if root == None:
            return 0
        left_depth = self.tree_depth(root.lchild)
        right_depth = self.tree_depth(root.rchild)
        return max(left_depth, right_depth) + 1


if __name__ == "__main__":
    str = "abd#g###ce##fh###"
    data = list(str)
    binary_tree = BinaryTree(data)
    root = binary_tree.pre_order_create()
    print("树的深度")  # 树的深度
    tree_depth = binary_tree.tree_depth(root)
    print(tree_depth)
