#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

链接： https://leetcode-cn.com/problems/generate-parentheses/
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        """
        思路： dfs + 剪枝

        剪枝条件： 左括号 >= 右括号
            1。 左括号没有使用完 就可以放入 左括号
            2。 左括号大于右括号
        """

        path, result = "", []
        self.dfs(n, 0, 0, path, result)
        return result

    def dfs(self, n, left, right, path, result):

        if left == n and right == n:
            result.append(path)
            return

        # 左括号 大于 0 就可以放入 左括号
        if left < n:
            self.dfs(n, left + 1, right, path + "(", result)
        #
        if left > right and right < n:
            self.dfs(n, left, right + 1, path + ")", result)


if __name__ == '__main__':
    k = 3
    rst = Solution().generateParenthesis(k)
    print("result is", rst)
