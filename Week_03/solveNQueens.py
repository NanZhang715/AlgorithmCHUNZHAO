#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例：
    输入：n = 4
    输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    解释：如上图所示，4 皇后问题存在两个不同的解法。

链接：https://leetcode-cn.com/problems/n-queens
"""
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        思路： dfs
              每层放入一个 Q，向下递归，直到最后一层，每层都判断是否合法
              col, diag1, diag2 分别用来判断 列，两个对角线是否能被攻击到

        - 对角线驱去重方案：
           "dale diagonals": row - column = constant
           "hill diagonals": row + column = constant

         时间复杂度：O(n!)
         空间复杂度  O(n)

        """
        self.n = n
        path, result = [], []
        self.dfs(0, [], [], [], path, result)
        return result

    def dfs(self, n, col, diag1, diag2, path, result):
        """
            n : 等于当前递归的深度，即行数，单调递减，用于递归终止
            col: 标记已使用过的列
            diag1 : 标记已使用过的对角线 hill diagonals
            diag2 : 标记已使用过的对角线 dale diagonals
            path : 每层合法的摆放位置
            result : 最终输出结果
        """

        if n == self.n:
            result.append(path)
            return

        for j in range(self.n):  # 递归遍历每列
            if j not in col and n + j not in diag1 and n - j not in diag2:
                self.dfs(
                    n + 1,
                    col + [j],
                    diag1 + [n + j],
                    diag2 + [n - j],
                    path + ["." * j + 'Q' + "." * (self.n - j - 1)], result
                )


if __name__ == '__main__':
    n = 4
    rst = Solution().solveNQueens(n)
    print(rst)


