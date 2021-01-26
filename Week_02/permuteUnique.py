#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

链接：https://leetcode-cn.com/problems/permutations-ii
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        思路： dfs + 剪枝

        剪枝：
            1。 判断是否重复
            2。 先排序，再判断后一个元素是否用过
        """
        path, result = [], []
        self.dfs(nums, path, result)
        return result

    def dfs(self, nums, path, result):

        if not nums:
            result.append(path)
            return

        for s in range(len(nums)):
            if path + [nums[s]] in result:
                continue
            self.dfs(nums[:s] + nums[s + 1:], path + [nums[s]], result)


if __name__ == '__main__':
    nums = [3, 3, 0, 3]
    rst = Solution().permuteUnique(nums)
    print("result is", rst)
