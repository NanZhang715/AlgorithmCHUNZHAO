#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。
链接：https://leetcode-cn.com/problems/two-sum

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for k, v in enumerate(nums):
            if target - v in nums and nums.index(target-v) != k:
                return [k, nums.index(target - v)]


if __name__ == '__main__':
    nums, target = [2, 7, 11, 15], 9
    rst = Solution().twoSum(nums,  target)
    print("result is", rst)
