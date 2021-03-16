#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

示例 1：

输入：matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

输出：[
    [1,4,7],
    [2,5,8],
    [3,6,9]]

链接：https://leetcode-cn.com/problems/transpose-matrix/
"""
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        思路： 转置的定义为行列互换
        """
        m, n = len(matrix), len(matrix[0])  # 行数， 列数
        rst = [[0]*m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                rst[j][i] = matrix[i][j]
        return rst


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6]]
    rst = Solution().transpose(matrix)
    print("result is", rst)
