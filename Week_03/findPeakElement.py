#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
162. 寻找峰值
峰值元素是指其值大于左右相邻值的元素。
给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。

示例 1：
    输入：nums = [1,2,3,1]
    输出：2
    解释：3 是峰值元素，你的函数应该返回其索引 2。

提示：
    - 1 <= nums.length <= 1000
    - 231 <= nums[i] <= 231 - 1
    - 对于所有有效的 i 都有 nums[i] != nums[i + 1]

链接：https://leetcode-cn.com/problems/find-peak-element
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        思路： 二分， 因为 nums[0]= nums[-1]= - inf, 所以只要nums[i] 比周围的值大，沿着该方向就可以找到峰值
        """
        if not nums:
            return None
        nums = [-float("inf")] + nums + [-float("inf")]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid - 1
            else:
                if nums[mid] > nums[mid + 1]:  # peak 在左侧
                    right = mid - 1
                else:
                    left = mid + 1

        return left

    # def findPeakElement_linear(self, nums: List[int]) -> int:
    #     """
    #     思路：
    #         （1） 线性查找，相邻的两个数字不相同，
    #             - 单调上升， peak = 0
    #             - 单调下降， peak = -1
    #             - peak 在中间，
    #         （2） 二分查找 nums[i] != nums[i + 1]
    #     """
    #     n = len(nums)
    #     for i in range(n):
    #         print(nums[i], nums[i+1])
    #         if nums[i] > nums[i + 1]:
    #             return i
    #     return n - 1


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    rst = Solution().findPeakElement(nums)
    print("result is", rst)
