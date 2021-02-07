#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
221. 最大正方形
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：

输入：matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
        ]
输出：4
链接：https://leetcode-cn.com/problems/maximal-square/
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        思路：动态规划，
            dp[i][j] 表示，以 [i][j] 为右下角的 正方的边长，

            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        时间复杂度：O(mn)
        空间复杂度：O(mn)
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if not i and not j:
                        dp[i][j] = 1
                    elif not i or not j: # 第一行
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) +1

                    max_side = max(max_side, dp[i][j])

        return max_side * max_side


if __name__ == '__main__':
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    rst = Solution().maximalSquare(matrix)
    print("result is", rst)





