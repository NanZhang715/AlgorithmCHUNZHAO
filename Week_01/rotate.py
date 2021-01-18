#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
示例：
    输入: nums = [1,2,3,4,5,6,7], k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右旋转 1 步: [7,1,2,3,4,5,6]
    向右旋转 2 步: [6,7,1,2,3,4,5]
    向右旋转 3 步: [5,6,7,1,2,3,4]

链接：https://leetcode-cn.com/problems/rotate-array
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        思路： 三步反转
        1。反转 nums[:k+1], 例如 [4，3，2，1] + [:]
        2. 反转 nums[k+1:], [:] + [7, 6, 5]
        3. 反转 nums [5, 6, 7, 4, 3, 2, 1]
        """
        n = len(nums)
        k = k%n
        self.reverse(nums, 0, n - k - 1)
        self.reverse(nums, n - k, n - 1)
        self.reverse(nums, 0, n - 1)

    def reverse(self, nums, left, right):
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums, k = [1, 2, 3, 4, 5, 6, 7], 3
    Solution().rotate(nums, k)
    print("result is", nums)
