# coding: utf-8
import random

'''
选择排序（Select Sort）

思路：
1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
2.然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3.以此类推，直到所有元素均排序完毕。
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
# Select sort
# Time complexity:
#   - Best: O(n^2)
#   - Average: O(n^2)
#   - Worst: O(n^2)
# Space complexity: O(1)
# Stability: Yes
#############################

class Sort():
    def __init__(self):
        pass

    def select_sort(self,data_list):
        """选择排序"""
        length = len(data_list)
        # 需要进行n-1次选择操作
        for i in range(length-1):
            # 记录最小位置
            min = i
            # 从i+1位置到末尾选择出最小数据
            for j in range(i+1,length):
                if data_list[j] < data_list[min]:
                    min = j
            # 如果选择出的数据不在正确位置，进行交换
            if i != min:
                data_list[i],data_list[min] = data_list[min],data_list[i]

if __name__ == '__main__':
    data_list = [54,26,93,17,77,31,44,55,20]
    # data_list = []
    # for i in range(100):
    #     data_list.append(random.randint(0, 100))
    sort = Sort()
    print("排序前")
    print(data_list)
    print("选择排序")
    sort.select_sort(data_list)
    print(data_list)

