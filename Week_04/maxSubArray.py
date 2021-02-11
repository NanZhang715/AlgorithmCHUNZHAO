#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例 1：

    输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
    输出：6
    解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        思路：贪心
        局部最优 与 全家最优

        时间复杂度: O(n)
        空间复杂度: O(1)
        """

        if not nums:
            return 0

        cur, max_sum = nums[0], nums[0]
        for s in nums[1:]:
            cur = max(cur + s, s)  # 之前数组之和，和当前元素的大小
            max_sum = max(max_sum, cur)
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    rst = Solution().maxSubArray(nums)
    print("result is", rst)
