#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
347. 前 K 个高频元素
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

    输入: nums = [1,1,1,2,2,3], k = 2
    输出: [1,2]

链接：https://leetcode-cn.com/problems/top-k-frequent-elements/
"""

import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:

        """
        思路：
        （1） 堆排序, 维护一个 k 的小顶堆
            时间复杂度：O(n + nlogk) 即 O(nlogk)
            空间复杂度：O(n + k), 哈希表 O(n), 最小堆 O(k)， 即 O(n)

        （2） 改进排序， 主要找到前 k 的即可，不需要对前 k 进行排序
            平均时间复杂度：O(n)
            空间复杂度：O(n)
        """
        freq_dict = {}
        for s in nums:
            freq_dict[s] = freq_dict.get(s, 0) + 1

        min_heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [s[1] for s in min_heap]

    def topKFrequent_partition(self, nums: List[int], k: int) -> List[int]:

        arr = [(v, k) for k, v in Counter(nums).items()]
        n = len(arr)
        self.find_k(arr, 0, n, n - k)
        return [s[1] for s in arr][-k:]

    def find_k(self, nums, beg, end, k):

        while beg < end:
            pivot = self.partition(nums, beg, end)
            if pivot == k:
                return
            elif pivot > k:
                end = pivot
            else:
                beg = pivot + 1

    def partition(self, nums, beg, end):

        pivot_index = beg
        pivot = nums[beg][0]  # 此处易出现失误
        left, right = pivot_index + 1, end - 1
        while True:
            while left <= right and nums[left][0] <= pivot:
                left += 1
            while left <= right and nums[right][0] > pivot:
                right -= 1

            if left > right:
                break
            else:
                nums[left], nums[right] = nums[right], nums[left]

        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]

        return right


if __name__ == '__main__':
    # nums, k = [5, 3, 1, 1, 1, 3, 73, 1], 1
    nums, k = [1, 1, 1, 2, 2, 3], 2
    rst = Solution().topKFrequent_partition(nums, k)
    print("result is", rst)
