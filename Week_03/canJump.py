#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

示例1：

    输入：nums = [2,3,1,1,4]
    输出：true
    解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

链接：https://leetcode-cn.com/problems/jump-game
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        思路：贪心
        每次保留当前能到达的最远位置，最后判断是否大于 len(nums) -1

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        reach, n = 0, len(nums)-1

        for k, v in enumerate(nums[:-1]):
            if k <= reach:
                reach = max(reach, k + v)
            else:
                return False
        return reach >= n


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    rst = Solution().canJump(nums)
    print("result is", rst)