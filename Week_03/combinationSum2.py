#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个数组 candidates 和一个目标数 target，找出 candidates 中所有可以使数字和为 target的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。

    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]

链接：https://leetcode-cn.com/problems/combination-sum-ii
"""
from typing import List


class Solution:
    def combinationSum2_dfs(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        思路： dfs 组合问题，不能重复使用, 类似排列组合
             - start 每次 增加 1， 标记已经使用过的元素，下一循环 从 start + 1 位置开始搜索

              剪枝
             - 为了避免重复，首先对数据进行排序
             - 加入的元素之和不能大于target， target - candidate[s]
             - 每次遍历开始的索引大于 上一层 range(start, n)
             - 同层不能使用一样的元素，不同层可以使用一样的元素
        """

        n, path, result = len(candidates), [], []
        candidates.sort()
        print(candidates)
        self.dfs(n, candidates, 0, target, path, result)
        return result

    def dfs(self, n, candidates, start, target, path, result):

        # 返回条件
        if target == 0:
            result.append(path)
            return

        for s in range(start, n):
            if candidates[s] > target:
                return

            if s > start and candidates[s] == candidates[s - 1]:
                continue

            self.dfs(n, candidates, s + 1, target - candidates[s], path + [candidates[s]], result)


if __name__ == '__main__':
    candidates, target = [10, 1, 1, 2, 7, 6, 5], 8
    rst = Solution().combinationSum2_dfs(candidates, target)
    print("result is ", rst)
