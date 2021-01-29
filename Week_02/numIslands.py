#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

链接：https://leetcode-cn.com/problems/number-of-islands
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        思路：dfs

        1。 从 (i, j) 向上下左右，(i+1, j) (i, j+1)  (i-1,j)(i,j-1) 做深度 搜索
        2。 终止条件：
            - (i, j) 过界
            - grid[i][j] == 0
        3。 搜索过的岛屿 grid[i][j] 置为 0， 以防重复计算

        主方法：
            - 遍历 matrix，遇到 grid[i][j] == 1 开始执行 dfs
            - count += 1

        时间复杂度：O(MN) matrix 中每个位置都要搜索
        空间复杂度：O(MN), 全部为陆地时，递归栈的空间为 MN
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):

        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)


if __name__ == '__main__':

    matrix = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    rst = Solution().numIslands(matrix)
    print("result is", rst)
