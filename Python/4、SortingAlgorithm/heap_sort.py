# coding: utf-8
import random

'''
堆排序（Heap Sort）

思路：
1. build heap
2. swap with the element on the right side (keep bigger element on the right)
3. rebuild heap(heapify)
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
# Heap sort
# Time complexity:
#   - Best: O(nlogn)
#   - Average: O(nlogn)
#   - Worst: O(nlogn)
# Space complexity: O(1)
# Stability: No
#############################

class Sort():
    def __init__(self,data_list):
        self.data_list = data_list
        self.length = len(data_list)

    def heap_sort(self):
        """堆排序"""
        self.build_max_heap(self.data_list) # 建堆
        for i in range(self.length-1, -1, -1): # 将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆。
            self.data_list[0],self.data_list[i] = self.data_list[i],self.data_list[0]
            self.heapify(self.data_list,0,i)

    def build_max_heap(self, seq):
        """建立大顶堆"""
        for i in range(self.length//2-1, -1, -1): # 从最后一个非叶子结点self.length//2-1开始,从左至右，从下至上遍历进行调整，使得根节点大于左右子节点。
            self.heapify(seq,i,self.length)

    def heapify(self,seq, index, length):
        max_index = index
        left = index *2 + 1
        right = index *2 + 2
        if left < length and seq[left] > seq[max_index]: # 如果左子树的值比根节点的值大，则最大值为左子树的值
            max_index = left
        if right < length and seq[right] > seq[max_index]: # 如果右子树的值比根节点的值大，则最大值为右子树的值
            max_index = right
        if max_index != index:
            seq[index],seq[max_index] = seq[max_index],seq[index]
            self.heapify(seq,max_index,length)

if __name__ == '__main__':
    data_list = [54,26,93,17,77,31,44,55,20]
    # data_list = []
    # for i in range(100):
    #     data_list.append(random.randint(0, 100))
    sort = Sort(data_list)
    print("排序前")
    print(data_list)
    print("堆排序")
    sort.heap_sort()
    print(data_list)

