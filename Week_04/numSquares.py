#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定正整数 n，找到若干个完全平方数（比如  1, 4, 9, 16, ...）使得它们的和等于 n。
你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，
而 3 和 11 不是。

链接：https://leetcode-cn.com/problems/perfect-squares
"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        思路：动态规划, 类似硬币找零
        c 是待用 完全平方数
        dp[i] = min(dp[i-c] +1)

        初始条件：f(0) = 0
        """
        square_nums = [s*s for s in range(1, int(n**0.5)+1)]
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for s in square_nums:
                if i >= s:
                    dp[i] = min(dp[i], dp[i-s] + 1)
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    n = 2
    rst = Solution().numSquares(n)
    print("result is", rst)
