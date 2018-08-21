# coding: utf-8
import random

'''
插入排序（Insert Sort）

思路：
1.从第一个元素开始，该元素可以认为已经被排序；
2.取出下一个元素，在已经排序的元素序列中从后向前扫描；
3.如果该元素（已排序）大于新元素，将该元素移到下一位置；
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5.将新元素插入到该位置后；
6.重复步骤2~5。
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
# Insertion sort
# Time complexity:
#   - Best: O(n)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################

class Sort():
    def __init__(self):
        pass

    def insert_sort(self,data_list):
        """插入排序"""
        for i in range(1,len(data_list)):
            for j in range(i,0,-1):
                if data_list[j] < data_list[j-1]:
                    data_list[j],data_list[j-1] = data_list[j-1],data_list[j]

if __name__ == '__main__':
    data_list = [54,26,93,17,77,31,44,55,20]
    # data_list = []
    # for i in range(100):
    #     data_list.append(random.randint(0, 100))
    sort = Sort()
    print("排序前")
    print(data_list)
    print("插入排序")

    sort.insert_sort(data_list)
    print(data_list)

