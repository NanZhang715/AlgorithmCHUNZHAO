#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
130. 被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。
    任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的

链接：https://leetcode-cn.com/problems/surrounded-regions/
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        思路： dfs

        边界条件：
            1。 不在边界上
            2。 不与边界上 "O" 相连的 "O"， 将会被填充
        """
        if not board:
            return board

        m, n = len(board), len(board[0])

        # 第一列和最后一列
        for i in range(m):
            self.dfs(i, 0, board)
            self.dfs(i, n-1, board)

        # 第一行和最后一行
        for j in range(n):
            self.dfs(0, j, board)
            self.dfs(m-1, j, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, m, n, board):

        if not 0 <= m < len(board) or not 0 <= n < len(board[0]) or board[m][n] != "O":
            return

        if board[m][n] == "O":
            board[m][n] = "A"
            self.dfs(m + 1, n, board)
            self.dfs(m - 1, n, board)
            self.dfs(m, n + 1, board)
            self.dfs(m, n - 1, board)


if __name__ == '__main__':
    # board = [
    #     ["X", "X", "X", "X"],
    #     ["X", "O", "O", "X"],
    #     ["X", "X", "O", "X"],
    #     ["X", "O", "X", "X"]]
    board = [["O"]]
    Solution().solve(board)
    for s in range(len(board)):
        print(board[s])
