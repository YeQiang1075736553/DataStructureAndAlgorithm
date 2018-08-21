# coding: utf-8
import random

'''
归并排序（Merge Sort）

思路：
1.把长度为n的输入序列分成两个长度为n/2的子序列；
2.对这两个子序列分别采用归并排序；
3.将两个排序好的子序列合并成一个最终的排序序列。
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
# Merge sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(nlogn)
# Space complexity: O(n)
# Stability: Yes
#############################

class Sort():
    def __init__(self):
        pass

    def merge_sort(self,data_list):
        """归并排序"""
        if len(data_list) <= 1:
            return data_list
        # 二分分解
        mid = len(data_list)//2
        left = self.merge_sort(data_list[:mid])
        right = self.merge_sort(data_list[mid:])
        # 合并
        return self.merge(left,right)

    def merge(self,left,right):
        # 合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组
        result = []
        while len(left) > 0 and len(right) > 0:
            # 为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
        result += left
        result += right
        return result

if __name__ == '__main__':
    data_list = [54,26,93,17,77,31,44,55,20]
    # data_list = []
    # for i in range(100):
    #     data_list.append(random.randint(0, 100))
    sort = Sort()
    print("排序前")
    print(data_list)
    print("堆排序")
    result = sort.merge_sort(data_list)
    print(result)

