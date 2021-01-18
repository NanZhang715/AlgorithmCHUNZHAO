#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        思路：双指针
        left： 左侧均为非零数字
        right：一直遍历数组, nums[right] 指向非零，交换左右指针
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


if __name__ == '__main__':

    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print("result is", nums)