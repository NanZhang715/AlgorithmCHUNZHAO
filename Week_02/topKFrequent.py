#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

链接：https://leetcode-cn.com/problems/top-k-frequent-elements/
"""
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        思路：
        时间复杂度：O(Nlogk)
        空间复杂度：O(N)。哈希表的大小为 O(N)，而堆的大小为 O(k)，共计为 O(N)。
        """

        freq_dict, heap = {}, []
        for s in nums:
            freq_dict[s] = freq_dict.get(s, 0) + 1

        for char, v in freq_dict.items():
            heapq.heappush(heap, (v, char))
            if len(heap) > k:
                heapq.heappop(heap)

        return [s[1] for s in heap]


if __name__ == '__main__':
    nums, k = [1, 1, 1, 2, 2, 3], 2
    rst = Solution().topKFrequent(nums, k)
    print("result is", rst)
