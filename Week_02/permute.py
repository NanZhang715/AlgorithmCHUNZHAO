#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

链接：https://leetcode-cn.com/problems/permutations

"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        path, result = [], []

        self.dfs(nums, path, result)
        return result

    def dfs(self, nums, path, result):

        if not nums:
            result.append(path)
            return

        for s in range(len(nums)):
            self.dfs(nums[:s] + nums[s + 1:], path + [nums[s]], result)


if __name__ == '__main__':
    nums = [1, 2, 3]
    rst = Solution().permute(nums)
    print("result is", rst)
