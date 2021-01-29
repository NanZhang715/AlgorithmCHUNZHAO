#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
定义：
    操作逻辑为树结构，但是以数组的形式进行存储
    "A heap is one of the tree structures and represented as a binary tree"

性质：
    （1）根节点 root， 数组索引从 1 开始， root_node | 1
    （2）父节点 i/2, 返回父节点 , parent_node | i/2 
    （3）左节点：left_inidex = 2 * i,  left_node | 2i
    （4）右节点：right_inidex = (2 * i) + 1,  right_node | 2i +1

操作：
    （1）heapify: 是该节点以及子节点满足堆的性质
        "make some node and its descendant nodes meet the heap property"

    （2）build_heap: 从一个随机数组中构建一个堆, 类似 heap_sort
        "produce a heap from an arbitrary array"
            1. 从最后一个父节点，依次向上heapify
        伪代码：
        build_min_heap(array)
                for i=n/2 downto 1
                do min_heapify(array, i)

    （3）插入：新元素放入最后，依次向上进行交换  shift_up
    （4）删除：删除堆顶元素，将末尾数据放入 堆顶，依次向下进行交换 shift_down
            1. 交换 arr[0] 和 arr[-1]
            2. arr.pop() 删除 arr[-1]
            3. shift_down


时间复杂度：
    （1）heapify: O(logn): 每次交换操作都是和子节点进行对比，复杂度为 tree 的高度
    （2）build_heapify: O(n)
        heap 中节点数量是 n，树高为 h(logn), 根节点下面的两个节点，需要向下调整 logn -1, 第三层的4个节点需要调整
        logn -2
                第一层的节点数量为 2^0 * logn
                第一层的节点数量为 2^1 * logn -1
                第n层的节点数量为 2^h
        构造 heap 中需要对每个元素进行 heapify
        sum = 1 * logn + 2*logn -1 + 4* logn -2... +
        2sum = 2 * logn + 4*logn -1 +8*logn -2... +
        2sum -sum = 2 + 4 + 8 + 2^logn = 2n
"""


class MinHeap:

    def __init__(self):
        """
        初始化数组，以及 heap_size
        """
        self.heap_list = [0]
        self.heap_size = 0

    def shift_up(self, i):
        """
        与 parent node 进行对比， 向上交换元素， 保持 heap 的性质
        """
        # While the element is not the root
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[(i - 1) // 2], self.heap_list[i]
            i = i // 2

    def push(self, n):
        """
        新元素加入 heap，更新 size， 放入最后，依次向上交换
        """
        self.heap_list.append(n)
        self.heap_size += 1
        self.shift_up(self.heap_size)

    def shift_down(self, i):

        """
        与子节点进行对比交换，，保持堆的性质,
        """
        # 如果该节点至少有一个子节点
        while 2 * i + 1 <= self.heap_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def min_child(self, i):

        # 如果只有左子节点
        if (2 * i) + 1 > self.heap_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return i * 2
            return (i * 2) + 1

    def pop(self):

        if not self.heap_size:
            return "Empty heap"

        root = self.heap_list[1]
        self.heap_list[1], self.heap_list[-1] = self.heap_list[-1], self.heap_list[1]
        self.heap_list.pop()
        self.heap_size -= 1
        self.shift_down(1)

        return root


if __name__ == '__main__':

    my_heap = MinHeap()
    my_heap.push(5)
    my_heap.push(6)
    my_heap.push(7)
    my_heap.push(9)
    my_heap.push(13)
    my_heap.push(11)
    my_heap.push(10)
    print(my_heap.heap_list)
    print(my_heap.pop())  # removing min node i.e 5
    print(my_heap.pop())
    print(my_heap.heap_list)
