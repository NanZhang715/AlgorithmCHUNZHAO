#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

from typing import List


class Solution:

    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        path, result = [], []
        self.dfs(nums, 0, path, result)
        return result

    def dfs(self, nums, start, path, result):

        # 所有结果都为有效结果，全部放入
        result.append(path)

        for s in range(start, len(nums)):
            self.dfs(nums, s + 1, path + [nums[s]], result)

    def subsets_lexi(self, nums: List[int]) -> List[List[int]]:
        """
        思路：bfs 或者 binmask，后者的复杂度较低

        时间复杂度：O(n * 2^n), 一共右 2^n 个状态 ，每个状态需要 O(n) 构造子集
        空间复杂度：O(n)， 构造子集需要的临时数组
        """
        if not nums:
            return []

        n, rst = len(nums), []
        for s in range(2 ** n, 2 ** (n + 1)):
            bin_mask = bin(s)[3:]

            rst.append([nums[i] for i in range(n) if bin_mask[i] == "1"])

        return rst


if __name__ == '__main__':
    nums = [1, 2, 3]
    rst = Solution().subsets_dfs(nums)
    print("result is", rst)
