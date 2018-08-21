# coding: utf-8
import random

'''
冒泡排序（Bubble Sort）

思路：
1.比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3.针对所有的元素重复以上的步骤，除了最后一个；
4.重复步骤1~3，直到排序完成。
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
# Bubble sort
# Time complexity:
#   - Best: O(n)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################

class Sort():
    def __init__(self,data_list):
        self.data_list = data_list
        self.length = len(data_list)

    def bubble_sort(self):
        """冒泡排序"""
        list = self.data_list
        for i in range(self.length-1,0,-1):
            for j in range(i):
                if list[j] > list[j+1]:
                    list[j],list[j+1] = list[j+1],list[j]
        return list

    def bubble_sort_advanced(self):
        """改进冒泡排序，,当某一轮跑完，不存在数据交换时，代表已排序完成，此时退出,时间复杂度为O(n^2)"""
        list = self.data_list
        flag = True # 记录是否发生交换信息
        for i in range(self.length-1,0,-1):
            # 如果上一轮存在数据交换
            if flag:
                flag = False
                for j in range(i):
                    if list[j] > list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j]
                        flag = True # 如果有数据交换
            # 否则，目前序列已经排序完毕
            else:
                break
        return list

    def bubble_sort_advanced_2(self):
        """双向冒泡排序（鸡尾酒排序），因为未发生交换操作的区域是有序的，故每轮扫描下来可以更新上下边界，减少扫描范围"""
        list = self.data_list
        low = 0
        high = self.length-1
        while low < high:
            swap_pos = low # 先假设最后一次发生交换操作的位置为low
            for i in range(low,high): # 顺序扫描list[low...high-1]
                if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
                    swap_pos = i
            high = swap_pos
            for i in range(high,low,-1): # 逆序扫描list[low+1...high]
                if list[i] < list[i-1]:
                    list[i],list[i-1] = list[i-1],list[i]
                    swap_pos = i
            low = swap_pos
        return list

if __name__ == '__main__':
    data = [54,26,93,17,77,31,44,55,20]
    sort = Sort(data)
    # data_list = []
    # for i in range(100):
    #     data_list.append(random.randint(0, 100))

    # print("冒泡排序")
    # bubble_sort = sort.bubble_sort()
    # print(bubble_sort)

    # print("改进冒泡排序")
    # bubble_sort = sort.bubble_sort_advanced()
    # print(bubble_sort)

    print("双向冒泡排序")
    bubble_sort = sort.bubble_sort_advanced_2()
    print(bubble_sort)

