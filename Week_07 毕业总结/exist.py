#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
        思路： dfs， 遍历二维举证中所有点

        时间复杂度：O(mn*3**l)
        空间复杂度：O(mn)
        """
        m, n = len(board), len(board[0])
        path = ""
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word, path):
                        return True
        return False

    def dfs(self, m, n, step, board, word, path):

        # 返回 True 条件放在前面
        if step == len(word):
            return True

        if (not 0 <= m < len(board)) or (not 0 <= n < len(board[0])) or (board[m][n] != word[step]):
            return False

        board[m][n] = '*'
        result = self.dfs(m + 1, n, step + 1, board, word, path + board[m][n]) or \
                 self.dfs(m, n + 1, step + 1, board, word, path + board[m][n]) or \
                 self.dfs(m - 1, n, step + 1, board, word, path + board[m][n]) or \
                 self.dfs(m, n - 1, step + 1, board, word, path + board[m][n])

        board[m][n] = word[step]

        return result


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']]
    word = "ABCCED"
    rst = Solution().exist(board, word)
    print("result is", rst)

