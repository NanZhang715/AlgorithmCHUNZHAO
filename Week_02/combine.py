#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
链接：https://leetcode-cn.com/problems/combinations
"""

from typing import List

"""
dfs( n = 4, k = 2, start = 0, path = [], res = []) 
| index = 0
----dfs( n = 4, k = 2, start = 1, path  = [1], res = []) 
|   | index = 1
|   ----dfs ( n = 4, k = 2, start = 2, path  = [1, 2], res = [1, 2]) -> add & return
|   | index = 2
|   ----dfs( n = 4, k = 2, start = 3, path  = [1, 3], res = [[1, 2], [1, 3]]) -> add & return
|   | index = 3
|   ----dfs( n = 4, k = 2, start = 4, path  = [1, 4], res = [[1, 2], [1, 3], [1, 4]]) -> add & return
| index = 1
----dfs( n = 4, k = 2, start = 2, path  = [2], res = [[1, 2], [1, 3], [1, 4]]) 
|   | index = 2
|   ----dfs ( n = 4, k = 2, start = 3, path  = [2, 3], res = [[1, 2], [1, 3], [1, 4], [2, 3]]) -> add & return
|   | index = 3
|   ----dfs( n = 4, k = 2, start = 4, path  = [1, 4], res = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]) -> add & return
| index = 2
----dfs( n = 4, k = 2, start = 3, path = [3], res = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]]) 
|   | index = 3
|   ----dfs ( n = 4, k = 2, start = 4, path  = [3, 4], res = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]) -> add & return
| index = 3
----dfs( n = 4, k = 2, start = 4, path = [4], res = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4]]) -> return None

"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        path, result = [], []
        self.dfs(n, k, 0, path, result)
        return result

    def dfs(self, n, k, start, path, result):

        if len(path) == k:
            result.append(path)
            return

        for s in range(start, n):
            self.dfs(n, k, s + 1, path + [s + 1], result)


if __name__ == '__main__':
    n, k = 4, 3
    rst = Solution().combine(n, k)
    print("result is", rst)
