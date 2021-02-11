#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
    输入：coins = [1, 2, 5], amount = 11
    输出：3
    解释：11 = 5 + 5 + 1

链接：https://leetcode-cn.com/problems/coin-change/description/
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        思路： DP
        f(n) 为凑成金额为 n ，需要最少的硬币数量硬币
        动态转移方程：
            f(n) = min(f(n-c)) + 1
            其中 c 为硬币的面额
        边界条件：
            f(0) = 0 金额 0 不能由硬币组成
            f(1) = 1, f(2) = 1

         时间复杂度：O(n*c)
         空间复杂度：O(n)
        """
        if not coins:
            return -1

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        for s in range(1, amount + 1):
            for c in coins:
                if s >= c:
                    dp[s] = min(dp[s], dp[s - c]) + 1

        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':

    coins, target = [1, 2, 5], 11
    rst = Solution().coinChange(coins, target)
    print("result is ", rst)
