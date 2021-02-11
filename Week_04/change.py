#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。

示例 1:

    输入: amount = 5, coins = [1, 2, 5]
    输出: 4
    解释: 有四种方式可以凑成总金额:
            5=5
            5=2+2+1
            5=2+1+1+1
            5=1+1+1+1+1

链接：https://leetcode-cn.com/problems/coin-change-2
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        思路： DP，组合问题
            f(n, c) 凑成  金额 n 使用前n的硬币的组合数量。

        例如：
            0，   1，   2，   3，   4，   5
        1   0     1     1    1     1    1
        2   0     1     2    2     2    3
        5   0     1     2    2     2    4

        dp[0] = 1

        时间复杂度：O(amount * c)
        空间复杂度：O(amount)
        """

        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for s in range(amount+1):
                if s >= c:
                    dp[s] += dp[s-c]
        return dp[-1] if dp[-1] else 0


if __name__ == '__main__':
    amount, coins = 5, [1, 2, 5]
    rst = Solution().change(amount, coins)
    print("result is", rst)

