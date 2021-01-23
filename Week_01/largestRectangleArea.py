#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        思路：
        1。 暴力法
            依次遍历每个数据中每个元素，直到遇到右侧严格小于的元素，即为该元素为左边界
            可以得到的最大面积
        时间复杂度 O(n^2)
        空间复杂度 O(1)

        2. 单调栈 Monotone Stack
           通过暴力法可知只要找到比栈顶元素小的值，栈顶元素的面积就可以确定

           Area = height * width
           堆中放入元素为 索引，高度通过索引获得

           边界条件

        tick：为防止栈为空，或者遍历完栈内还有元素的情况发生，
              可在栈两端放入 哨兵 Sentinel，元素 0
    """
        max_area, stack = 0, []
        heights = [0] + heights + [0]  # 前后加哨兵元素

        for k, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:  # 元素大于栈顶元素
                max_stack_ids = stack.pop()
                print(stack, heights[stack[-1]])
                max_area = max(max_area, heights[max_stack_ids] * (k - stack[-1] - 1))  # 不算两边只取 中间的距离
            stack.append(k)
        return max_area


if __name__ == '__main__':
    nums = [2, 1, 5, 6, 2, 3]
    rst = Solution().largestRectangleArea(nums)
    print("result is", rst)
