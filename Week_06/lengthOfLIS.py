#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：
    输入：nums = [10,9,2,5,3,7,101,18]
    输出：4
    解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        思路：
            dp[i] 表示 nums[i] 位递增序列的长度，
            dp[i] = max(dp[:i-1 ]) + 1

        时间复杂福：O(n^2)
        空间复杂度：O(n)
        """
        if not nums:
             return 0

        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return dp[-1]


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    rst = Solution().lengthOfLIS(nums)
    print("result is", rst)