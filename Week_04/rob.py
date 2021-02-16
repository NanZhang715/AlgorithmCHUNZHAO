#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，
计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
    输入：[1,2,3,1]
    输出：4
    解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
         偷窃到的最高金额 = 1 + 3 = 4 。
链接：https://leetcode-cn.com/problems/house-robber/
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        思路： DP
            dp[i] 表示偷到第 i 个房屋时，获取的最大金额, 即
            (1) 偷第 i 家， dp[i-2] + nums[i]
            (2) 不偷第 i 家， dp[i-1]
        opt 方程：
            dp[i] = max(dp[i-1] , dp[i-2] + nums[i])
        边界条件：
            dp[0] = nums[0], dp[1] = nums[0] if dp[0] > dp[1] else dp[o]

        可以继续优化空间复杂度到 O(1)
        """

        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for s in range(2, len(nums)):
            dp[s] = max(dp[s-1], dp[s-2] + nums[s])

        return dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    rst = Solution().rob(nums)
    print("result is", rst)
