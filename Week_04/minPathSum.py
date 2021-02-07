#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

输入：grid = [
                [1,3,1],
                [1,5,1],
                [4,2,1]
            ]
输出：7
解释：因为路径 1 → 3 → 1 → 1 → 1 的总和最小。

链接：https://leetcode-cn.com/problems/minimum-path-sum/
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        """
        思路： 动态规划,
        对于 dp[i][j] 表示 [i][j] 之前路径之和
            dp[i][j] = min(dp[i -1][j], dp[i][j-1]) + grid[i][j]
        边界： 0<=i < M,  0<= j < N
        优化：直接修改原始矩阵，不需要额外空间

        时间复杂度：O(mn)
        空间复杂度：O(mn)
        """

        if not grid:
            return 0

        m, n = len(grid), len(grid[0]) # m 行， n 列

        for i in range(m):
            for j in range(n):
                if not i and not j:
                    grid[i][j] = grid[i][j]
                elif not i:  # 第一行只能沿着左边移动
                    grid[i][j] = grid[i][j-1] + grid[i][j]
                elif not j:  # 第一列只能向下移动
                    grid[i][j] = grid[i-1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
    rst = Solution().minPathSum(grid)
    print("result is", rst)
    print(grid)
