# coding: utf-8
import random

'''
希尔排序（Shell Sort）

思路：
1. 先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序
2. 然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
参见 https://blog.csdn.net/yeqiang19910412/article/details/81482061

编程环境：
Python3.5.2

作者：
CSDN博客：https://my.csdn.net/yeqiang19910412
Github：https://github.com/YeQiang1075736553

日期：
2018.8.13
'''

#############################
# Shell sort
# Time complexity:
#   - Best: O(n log^2 n)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: No
#############################

class Sort():
    def __init__(self):
        pass

    def shell_sort(self, data_list):
        """希尔排序"""
        length = len(data_list)
        increment = length // 2
        while increment > 0:
            for i in range(increment,length):
                # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
                j = i
                while j >= increment and data_list[j-increment] > data_list[j]:
                    data_list[j-increment],data_list[j] = data_list[j],data_list[j-increment]
                    j -= increment
            # 得到新的步长
            increment = increment//2

if __name__ == '__main__':
    data_list = [54,26,93,17,77,31,44,55,20]
    # data_list = []
    # for i in range(100):
    #     data_list.append(random.randint(0, 100))
    sort = Sort()
    print("排序前")
    print(data_list)
    print("希尔排序")
    sort.shell_sort(data_list)
    print(data_list)

