#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1277. 统计全为 1 的正方形子矩阵
给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。

示例 1：
    输入：matrix =
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
    输出：15
解释：
    边长为 1 的正方形有 10 个。
    边长为 2 的正方形有 4 个。
    边长为 3 的正方形有 1 个。
    正方形的总数 = 10 + 4 + 1 = 15.
"""

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        """
        思路：动态规划
            dp[i][j] 表示，以 [i][j] 为右下角的 正方的边长，

            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        边界： 0< =i < M,  0<= j < N
        优化：直接修改原始矩阵，不需要额外空间

        1   1        1   0      1  1      0  1
        1  [2]       1  [1]     0 [1]     1 [1]

        min(1, 1, 1) + 1 = 2
        min(1, 0, 1) + 1 = 1

        时间复杂度：O(mn)
        空间复杂度：O(mn)
        """

        m, n = len(matrix), len(matrix[0])
        count = 0
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    # if not i and not j:
                    #     dp[i][j] = 1
                    if not i or not j:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                count += dp[i][j]
        return count

    def countSquares_opt(self, matrix: List[List[int]]) -> int:

        """
        思路：动态规划, 优化空间复杂度
        dp[i][j] 只与 matrix[i][j], min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) 这两个值有关

        时间复杂度：O(mn)
        空间复杂度：O(1)
        """

        m, n = len(matrix), len(matrix[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if not i or not j:
                        count += 1
                    else:
                        cell_value = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + matrix[i][j]
                        count += cell_value
                        matrix[i][j] = cell_value
        return count


if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    rst = Solution().countSquares_opt(matrix)
    print("result is", rst)
