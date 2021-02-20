#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
713. 乘积小于K的子数组
给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

链接： https://leetcode-cn.com/problems/subarray-product-less-than-k/
"""

from typing import List


class Solution:
    def numSubarrayProductLessThanK_dp(self, nums: List[int], k: int) -> int:
        """
        思路： DP，超时
        """

        if not nums:
            return 0

        n, count = len(nums), 0
        dp = [[1] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = dp[i][j-1] * nums[j]

                if dp[i][j] < k:
                    count += 1

        return count

    def numSubarrayProductLessThanK_window(self, nums: List[int], k: int) -> int:
        """
        思路：滑动窗口 + 二分法
        对于 每个 right， nums[left], nums[left + 1], nums[left +2] ... nums[right]
        [0, right] 是单调递增的，找到 最大 sub_max < k

        时间复杂度： O(n*logn)
        空间复杂度： O(1)
        """
        if not nums:
            return 0

        left, count, product = 0, 0, 1
        for right in range(len(nums)):
            product *= nums[right]

            if product >= k:
                while product >= k and left <= right:
                    product /= nums[left]

            count += right - left + 1

        return count


if __name__ == '__main__':
    nums, k = [10, 5, 2, 6], 100
    rst = Solution().numSubarrayProductLessThanK_window(nums, k)
    print("result is", rst)