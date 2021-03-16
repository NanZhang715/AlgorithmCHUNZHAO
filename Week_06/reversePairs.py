#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
493. 翻转对
给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
你需要返回给定数组中的重要翻转对的数量。

示例 1:
    输入: [1,3,2,3,1]
    输出: 2
"""
from typing import List


class Solution:

    def __init__(self):
        self.reverse_count = 0

    def reversePairs(self, nums: List[int]) -> int:
        """
        思路： 归并排序的变形
         - 依次 split array
         - 合并时计算翻转对的数量, 即 逆序数 = left_逆序数 + right_逆序数 + cross_逆序数

         cross 计算：
            if 2 * right < left, 此时 right 的长度即为逆序的长度
        """

        self.merge_sort(nums)
        return self.reverse_count

    def merge_sort(self, nums):

        if len(nums) < 2:
            return nums

        mid = len(nums)// 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):

        rst = []
        while left and right:
            if left[-1] >= right[-1]:
                index = 0
                while index < len(right) and left[-1] > 2 * right[index]:
                    self.reverse_count += 1
                    index += 1
                    print(self.reverse_count, left, right)
                cur = left.pop()
            else:
                cur = right.pop()
            rst.insert(0, cur)

        if left:
            rst = left + rst
        if right:
            rst = right + rst
        return rst


if __name__ == '__main__':
    # nums = [1, 3, 2, 3, 1]
    nums = [-5, -5]
    rst = Solution().reversePairs(nums)
    print("result is", rst)

    rst = Solution().merge_sort(nums)
    print("result is", rst)
