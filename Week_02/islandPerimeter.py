#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个 row x col 的二维网格地图 grid ，其中：grid[i][j] = 1 表示陆地， grid[i][j] = 0 表示水域。
网格中的格子 水平和垂直 方向相连（对角线方向不相连）。整个网格被水完全包围，
但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

链接：https://leetcode-cn.com/problems/island-perimeter
"""

from typing import List


class Solution:
    def islandPerimeter_iter(self, grid: List[List[int]]) -> int:
        """
        思路：岛屿的周长就是岛屿方格和非岛屿方格相邻的边的数量
        判断 grid[i][j] 周围是否为水域，如果是则加入边长， 此题和岛屿数量非常相似，
             可以使用 dfs + 剪枝 或者 迭代每个位置判断周围是否存在水域，且迭代方法的时间复杂度与
             dfs 相同， 但是空间复杂度为 0(1)

        1. 迭代：
            - 遍历 O(MN) 每个位置
            - 当 grid[i][j] == "1" 时，判断周围是否为水域
                - 边界上的陆地，周长 += 边界
                - matrix内部陆地，周长 += 水域的数量

            时间复杂度 O(MN)
            空间复杂度 O(1)

        2. dfs:
            - 从 (i, j) 向上下左右，(i+1, j) (i, j+1)  (i-1,j)(i,j-1) 做深度 搜索
            - 终止条件：
                - (i, j) 过界
                - grid[i][j] == 0

            时间复杂度 O(MN)
            空间复杂度 O(MN)
        """

        if not grid:
            return 0

        m, n, perimeter = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0: perimeter += 1  # 上边界
                    if i == m - 1 or grid[i + 1][j] == 0: perimeter += 1  # 下边界
                    if j == 0 or grid[i][j - 1] == 0: perimeter += 1  # 左边界
                    if j == n - 1 or grid[i][j + 1] == 0: perimeter += 1  # 右边界

        return perimeter


class Solution:

    def islandPerimeter_recur(self, grid: List[List[int]]) -> int:

        """
        dfs:
            - 当 grid[i][j] == "1" 时，判断周围是非陆地的数量
            - 将遍历过的位置置为 2，防止无限循环
        主函数：
            - 每个位置都进行遍历
            - 返回结果
        """

        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += self.dfs(grid, i, j)

        # for s in range(len(grid)):
        #     print(grid[s])

        return perimeter

    def dfs(self, grid, i, j):

        # 边界上的边长返回 or 附近是水域
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
            return 1

        # 若该方格不是岛屿，直接返回
        if grid[i][j] != 1:
            return 0

        grid[i][j] = 2  # 代表已经访问过

        return self.dfs(grid, i + 1, j) + \
               self.dfs(grid, i, j + 1) + \
               self.dfs(grid, i - 1, j) + \
               self.dfs(grid, i, j - 1)


if __name__ == '__main__':
    grid = [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]
    ]

    # rst = Solution().islandPerimeter_iter(grid)
    rst = Solution().islandPerimeter_recur(grid)
    print("result is ", rst)
