#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

    输入: [2,3,1,1,4]
    输出: 2
    解释: 跳到最后一个位置的最小跳跃数是 2。
         从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

链接：https://leetcode-cn.com/problems/jump-game-ii/
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        思路： 贪心。此题和跳跃游戏相似，区别是此题要输出跳跃最少的次数
        可以维护一个 max_reach 即 end, k 到达 end 时， 就需要多跳跃一次

        每次在可跳范围内选择可以使得跳的更远

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        reach, end, count = 0, 0, 0

        for k, v in enumerate(nums[:-1]):
            if k <= reach:
                reach = max(reach, k+v)
                if k == end:
                    end = reach
                    count += 1
            else:
                return False
        return count


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    rst = Solution().jump(nums)
    print("result is", rst)
