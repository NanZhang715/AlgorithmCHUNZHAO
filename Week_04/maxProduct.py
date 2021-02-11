#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。

链接：https://leetcode-cn.com/problems/maximum-product-subarray/description/
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        思路：动态规划, 与最大子序列之和类似
        区别 负负得正，同时维护最大值, 最小值

        dp[i] = max(nums[i] * pre_max, nums[i] * pre_min, nums[i])

        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not nums:
            return 0

        global_max, pre_max, pre_min = nums[0], nums[0], nums[0]
        for s in nums[1:]:
            cur_max = max(s, pre_min*s, pre_max*s)
            cur_min = min(s, pre_min*s, pre_max*s)

            global_max = max(cur_max, global_max)

            pre_max = cur_max
            pre_min = cur_min

        return global_max


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    rst = Solution().maxProduct(nums)
    print("result is", rst)
