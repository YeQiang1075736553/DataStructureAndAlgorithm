# coding: utf-8
import random

'''
快速排序（Quick Sort）

思路：
1.从数列中挑出一个元素，称为 “基准”（pivot）；
2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
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
# Quick sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(n^2)
# Space complexity: O(logn) ~ O(n)
# Stability: No
#############################

class Sort():
    def __init__(self):
        pass
################################################################################
    def quick_sort(self,data_list,start,end):
        """快速排序"""
        if start < end:
            pivot = self.partition(data_list,start,end) # 基准位置
            self.quick_sort(data_list,start,pivot-1)
            self.quick_sort(data_list,pivot+1,end)

    def partition(self,data_list,start,end):
        # low为序列左边的由左向右移动的游标
        low = start
        # high为序列右边的由右向左移动的游标
        high = end
        # 设定起始元素为要寻找位置的基准值
        pivot_key = data_list[start]
        while low < high:
            # 如果low和high未重合，high指向的元素值大于基准值，则high向左移动
            while low < high and data_list[high] >= pivot_key:
                high -= 1
            # 将比基准值小的元素值交换到低端
            data_list[low], data_list[high] = data_list[high], data_list[low]
            while low < high and data_list[low] <= pivot_key:
                low += 1
            data_list[low], data_list[high] = data_list[high], data_list[low]
        return low # 返回基准值所在的位置

################################################################################
    def quick_sort_advanced(self,data_list,start,end):
        """三数取中法"""
        if start < end:
            low = start
            high = end
            mid = low + (high-low) // 2 # 向下取整
            # 使用三数取中法选择基准值
            if data_list[low] > data_list[high]:
                data_list[low],data_list[high] = data_list[high],data_list[low]
            if data_list[mid] > data_list[high]:
                data_list[mid], data_list[high] = data_list[high], data_list[mid]
            if data_list[mid] > data_list[low]:
                data_list[low], data_list[mid] = data_list[mid], data_list[low]
            # 此时，arr[mid] <= arr[low] <= arr[high],low的位置上保存这三个位置中间的值
            pivot = data_list[low]
            while low < high:
                while low < high and data_list[high] >= pivot:
                    high -= 1
                data_list[low],data_list[high] = data_list[high],data_list[low]
                while low < high and data_list[low] <= pivot:
                    low += 1
                data_list[low],data_list[high] = data_list[high],data_list[low]

            self.quick_sort_advanced(data_list,start,low-1)
            self.quick_sort_advanced(data_list,low+1,end)

################################################################################
    def quick_sort_advanced_2(self,data_list,start,end):
        """当待排序序列的长度分割到一定大小后，使用插入排序"""
        MAX_LENGTH_INSERT_SORT = 3 # 可变
        if (end - start) > MAX_LENGTH_INSERT_SORT:
            self.quick_sort_advanced(data_list,start,end)
        else:
            self.insert_set(data_list)

    def insert_set(self,data_list):
        # 从第二个位置，即下标为1的元素前开始向前插入
        for i in range(1,len(data_list)):
            for j in range(i,0,-1):
                if data_list[j-1] > data_list[j]:
                    data_list[j-1],data_list[j] = data_list[j],data_list[j-1]

################################################################################
    def quick_sort_advanced_3(self,data_list,start,end):
        MAX_LENGTH_INSERT_SORT = 3
        if (end - start) > MAX_LENGTH_INSERT_SORT:
            pivot = self.partition(data_list,start,end) # 基准位置
            self.quick_sort(data_list,start,pivot-1)
            start = pivot + 1
        else:
            self.insert_set(data_list)

if __name__ == '__main__':
    data_list = [54,26,93,17,77,31,44,55,20]
    # data_list = []
    # for i in range(100):
    #     data_list.append(random.randint(0, 100))
    sort = Sort()
    print("排序前")
    print(data_list)
    print("快速排序")
    sort.quick_sort(data_list,0,len(data_list)-1)
    print(data_list)

    # sort.quick_sort_advanced(data_list, 0, len(data_list) - 1)
    # print(data_list)

    # sort.quick_sort_advanced_2(data_list, 0, len(data_list) - 1)
    # print(data_list)

    # sort.quick_sort_advanced_3(data_list, 0, len(data_list) - 1)
    # print(data_list)