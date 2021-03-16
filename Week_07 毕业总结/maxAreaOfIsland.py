#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
695. 岛屿的最大面积
给定一个包含了一些 0 和 1 的非空二维数组 grid 。

一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。
你可以假设 grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

链接：https://leetcode-cn.com/problems/max-area-of-island/
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        """
        思路： 孤岛问题， 一次遍历每个岛的大小
        """

        if not grid:
            return 0

        maxArea, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(i, j, grid))

        return maxArea

    def dfs(self, m, n, grid):
        """
        1. 终止条件：越界 or grid[i][j] != 1
        2. 返回值 0
        3。 level task， 每层 area += 1
        """

        if not 0 <= m < len(grid) or not 0 <= n < len(grid[0]) or grid[m][n] != 1:
            return 0

        grid[m][n] = 0

        return self.dfs(m - 1, n, grid) + \
               self.dfs(m + 1, n, grid) + \
               self.dfs(m, n + 1, grid) + \
               self.dfs(m, n - 1, grid) + 1


if __name__ == '__main__':
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    rst = Solution().maxAreaOfIsland(grid)
    print("max area is", rst)
