#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：
    输入：m = 3, n = 7
    输出：28
链接：https://leetcode-cn.com/problems/unique-paths
"""
import math


class Solution:
    def uniquePaths_math(self, m: int, n: int) -> int:
        """
        思路：数学与 dp 两种方法

        （1） 数学
            一共移动 m + n - 2 步，结果为 选择 m - 1 此向下的路径
                (m-1)
                (m + n - 2)
        """

        return int(math.factorial(m + n - 2)/(math.factorial(m-1)*math.factorial(n-1)))

    def uniquePaths_dp(self, m: int, n: int) -> int:

        """
        思路：DP

        dp 方程：
            dp[i][i] = dp[i -1][j] + dp[i][j-1]
        边界条件：
            row = 0， 只能从左侧移动右
            col = 0， 只能从上移动到下
        """

        if not m and not n:
            return 0

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == '__main__':
    m, n = 3, 7
    rst = Solution().uniquePaths_dp(m, n)
    print("result is", rst)
