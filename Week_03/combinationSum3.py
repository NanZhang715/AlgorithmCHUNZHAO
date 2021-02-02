#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

    所有数字都是正整数。
    解集不能包含重复的组合。

输入: k = 3, n = 7
输出: [[1,2,4]]

链接：https://leetcode-cn.com/problems/combination-sum-iii
"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        思路： 与 combinationSum2 相同， 区别增加一条剪枝条件
        剪枝条件：
            - path 长度为 k
            - sum 为 n
        """

        path, result = [], []
        self.dfs(n, k, 0, path, result)
        return result

    def dfs(self, n, k, start, path, result):

        if len(path) == k and n == 0:
            result.append(path)
            return

        for s in range(start, 9):
            self.dfs(n - (s+1), k, s + 1, path + [s + 1], result)


if __name__ == '__main__':
    n, k = 7, 3
    rst = Solution().combinationSum3(k, n)
    print("result is ", rst)