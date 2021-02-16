#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，
系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：
    输入：nums = [2,3,2]
    输出：3
    解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
链接：https://leetcode-cn.com/problems/house-robber-ii/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        思路：DP， 198 打家劫舍的升级版本
        区别是房屋环形，代表第一个房屋和最后一个房屋只能偷取一个，扩展成二维的DP

        （1）在不偷窃第一个房子的情况下（即 nums[1:]nums[1:]），最大金额是 p1
        （2）在不偷窃最后一个房子的情况下（即 nums[:n-1]nums[:n−1]），最大金额是 p1
        （3） max(p1,p2)
        """

        if len(nums) < 2:
            return nums[0]

        return max(
            self.utils(nums[1:]),
            self.utils(nums[:-1])
        )

    def utils(self, nums):

        if not nums:
            return 0

        prev, cur = 0, 0
        for s in nums:
            prev, cur = cur, max(prev + s, cur)

        return cur


if __name__ == '__main__':
    nums = [2, 3, 2]
    rst = Solution().rob(nums)
    print("result is", rst)
