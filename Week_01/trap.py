#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

链接：https://leetcode-cn.com/problems/trapping-rain-water
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        思路：每个位置可接雨水 min(left_max,  right_max) - height
             1。分别 从左 右 遍历数据获取 left_max,  right_max 数据， 最后计算可求出结果
             时间复杂度 O(n)
             空间复杂度 O(n)

        可以做如下优化， 方案 1 中，left_max,right_max 只使用了一个， 可以使用双指针代替之前的数组,
        left_max 小于 right_max 时，左侧最小值确定，此时蓄水量由左侧决定
             方案 2。right_max[i] > left_max[i]， 由 left_max 决定
             时间复杂度 O(n)
             空间复杂度 O(1)
        """
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        ans = 0

        while left <= right:
            if left_max < right_max: # left_max 较小时， 由 蓄水量由 left_max 决定
                ans += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])

            else:
                ans += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    rst = Solution().trap(height)
    print("result is", rst)
