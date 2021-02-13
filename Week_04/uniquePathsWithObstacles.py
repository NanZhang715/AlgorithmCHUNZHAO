#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
63. 不同路径 II
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右

链接：https://leetcode-cn.com/problems/unique-paths-ii

"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        思路： DP，与路径问题相似。
             区别遇到障碍物时，该位置为 0

        时间复杂度：O(mn)
        空间复杂度：O(1)
        """

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # 边界条件
        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1
        for i in range(1, m):  # 第一列
            obstacleGrid[i][0] = 0 if obstacleGrid[i][0] and obstacleGrid[i-1][0] else 1
        for j in range(1, n):  # 第一行
            obstacleGrid[0][j] = 0 if obstacleGrid[0][j] and obstacleGrid[0][j-1] else 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]


if __name__ == '__main__':
    # obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    obstacleGrid = [[0]]
    rst = Solution().uniquePathsWithObstacles(obstacleGrid)
    print("result is", rst)



