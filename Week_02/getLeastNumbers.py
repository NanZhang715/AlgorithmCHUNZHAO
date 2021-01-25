#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
"""
import heapq
from typing import List

"""
    快排 和 堆排的比较
    
    1。快拍性能优于堆排序
    2。但是 快拍改变了原有数据，并且不适用于较大的数据集合或者是数据流
"""


class Solution:
    def getLeastNumbers_heap(self, arr: List[int], k: int) -> List[int]:
        """
        思路:
        1. 最大堆
            时间复杂度：O(nlogk)
            空间复杂度 O(k)
        """
        heap = []
        for s in arr:
            heapq.heappush(heap, -s)
            if len(heap) > k:
                heapq.heappop(heap)
        return [-i for i in heap]

    def getLeastNumbers_pivot(self, arr: List[int], k: int) -> List[int]:
        """
        思路:
        1. 快排序
            时间复杂度：O(n)
            空间复杂度 O(1)
        """
        if not arr:
            return []
        if k >= len(arr):
            return arr

        left, right = 0, len(arr)
        while left < right:
            pivot = self.patition(arr, left, right)
            if pivot == k:
                return arr[:k]
            elif pivot > k:  # 右边界不断逼近
                right = pivot
            else:  # pivot 小于 k，左边界不断试探
                left = pivot + 1

    def getLeastNumbers_pivot_recursive(self, arr: List[int], k: int) -> List[int]:
        """
        思路:
        1. 快排序 上面的快拍空间复杂度可以继续优化, 使用递归增加空间复杂度, 空间还时间，
        而是近似于二分法,
        做如下修改
            时间复杂度：O(logn)
            空间复杂度 O(n)
        """
        if not arr: return []
        if k >= len(arr): return arr

        return self.recursive_search(arr, k, 0, len(arr))

    def recursive_search(self, arr, k, left, right):

        pivot = self.patition(arr, left, right)  # pivot 为索引位置
        print(arr, pivot)
        print("left -> right", left, right)
        if pivot == k:
            return arr[:k]
        elif pivot > k:  # k 在 pivot 左侧， 因此在 lower parts 左半边查找
            return self.recursive_search(arr, k, left, pivot - 1)
        else:  # k 在 pivot 右侧 higher parts 寻找
            return self.recursive_search(arr, k - pivot, pivot + 1, right)

    def patition(self, nums, begin, end):

        """
         以 pivot 为界， 较大的值放右侧，较小的值放左侧，最终 返回 pivot 的索引
        """

        pivot_index = begin
        pivot = nums[pivot_index]
        left, right = pivot_index + 1, end - 1

        while True:
            if left <= right and nums[left] <= pivot:  # 相同的值，左指针也向右移动一步
                left += 1
            if right >= left and nums[right] > pivot:
                right -= 1

            if left > right:
                break
            else:
                nums[left], nums[right] = nums[right], nums[left]

        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # pivot放回列表

        return right


if __name__ == '__main__':
    nums, k = [0, 1, 2, 1], 1
    rst = Solution().getLeastNumbers_pivot_recursive(nums, k)
    print("result is", rst)
