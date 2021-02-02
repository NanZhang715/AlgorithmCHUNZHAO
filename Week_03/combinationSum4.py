#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
377. 组合总和 Ⅳ
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:
    nums = [1, 2, 3]
    target = 4

    所有可能的组合为：
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
请注意，顺序不同的序列被视作不同的组合。
因此输出为 7。

进阶：
    如果给定的数组中含有负数会怎么样？
    问题会产生什么变化？
    我们需要在题目中添加什么限制来允许负数的出现？

链接：https://leetcode-cn.com/problems/combination-sum-iv/
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int):
        """
        思路： 与 combinationSum 相似， 不过使用 dfs 会超时， 建议使用 dfs
        剪枝条件：
            - sum 为 target

        动态规划，与找零钱问题相似
            Time complexity: O(nm)
            Space complexity: O(m)
        """

        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for n in nums:
                if n <= i:
                    dp[i] += dp[i - n]
        return dp[-1]


if __name__ == '__main__':
    # nums, target = [1, 2, 3], 4
    nums, target = [4, 2, 1], 32
    rst = Solution().combinationSum4(nums, target)
    print("result is ", rst)
