#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标
相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，
那么下一步可以移动到下一行的下标 i 或 i + 1 。

示例 1：

    输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    输出：11
    解释：如下面简图所示：
       2
       3 4
       6 5 7
       4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
链接：https://leetcode-cn.com/problems/triangle
"""
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        思路：DP, 自底向上

            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

            为了减少空间复杂度，直接在 triangle 上进行修改
        """
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                print(triangle[i][j], triangle[i + 1][j], triangle[i + 1][j + 1], )
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    rst = Solution().minimumTotal(triangle)
    print("result is", rst)
