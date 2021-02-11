#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。

    输入：candidates = [2,3,6,7], target = 7,
    所求解集为：
    [
      [7],
      [2,2,3]
    ]

链接：https://leetcode-cn.com/problems/combination-sum
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        思路： dfs + 剪枝，依次选取 candidate 中的元素
            - 终止条件： sum > target
            - level task: 选取一个元素
            - 返回：数组

            剪枝：
                1，下一个选择的元素不能小与之前的放入的元素， 即不能选取比之前元素小的元素

          排序数组 [2,          3,           6,          7]

                                    path []
                             /       /         \    \
                  [2]               [3]       [6]   [7]
                /  \    \
            [2, 2]  [2, 3]  [2, 6] [2, 7]
            /   \
            [2,2, 2] [2, 2, 3] [2, 2, 6] [2, 2 ,7]

            时间复杂度：O((k+n)!）,  n 是 结果的数量， k 是最大candicate 重复的数量
            空间复杂度：O(target), 使用递归栈，最差情况需要递归 target 层
        """

        path, result = [], []
        candidates.sort()
        self.dfs(candidates, target, 0, path, result)
        return result

    def dfs(self, candidates, target, start, path, result):
        """
         在当前数字 start 位置
        """

        if target < 0:
            return

        if not target:
            result.append(path)
            return

        # 每个数字都可以无限选择, 所以下一层还可以重复选择，所以搜索的下标仍是 s
        for s in range(start, len(candidates)):
            self.dfs(candidates, target - candidates[s], s, path + [candidates[s]], result)


if __name__ == '__main__':
    candidates, target = [2, 3, 6, 7], 7
    rst = Solution().combinationSum(candidates, target)
    print("result is ", rst)
