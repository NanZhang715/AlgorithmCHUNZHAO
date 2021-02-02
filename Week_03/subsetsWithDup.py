#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
90. 子集 II
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

链接：https://leetcode-cn.com/problems/subsets-ii/
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        """
        思路：
            与组合题类似，不同点在于数组中存在重复数据，其他与 subset 基本一致
        去重思路：
            1。 排序
            2。 同层间不能存在重复，不同层可以重复
            时间复杂度：O(n * 2^n)
            空间复杂度：O(n)
        """
        path, result = [], []
        nums.sort()
        self.dfs(nums, 0, path, result)
        return result

    def dfs(self, nums, start, path, result):

        result.append(path)

        for s in range(start, len(nums)):
            if s > start and nums[s] == nums[s - 1]:  # 与上一个数字是否相同，如果相同则跳过
                continue
            self.dfs(nums, s + 1, path + [nums[s]], result)


if __name__ == '__main__':
    nums = [1, 2, 2]
    rst = Solution().subsetsWithDup(nums)
    print("result is", rst)
