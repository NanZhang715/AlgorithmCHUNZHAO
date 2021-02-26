#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例：
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

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

        2. 单调递增栈 Monotone Stack 找到更小的元素, 以 height[i] 为高度的矩形面积可以确定
           通过暴力法可知只要找到比栈顶元素小的值，栈顶元素的面积就可以确定

           Area = height * width
           堆中放入元素为 索引，高度通过索引获得

           矩形高度为 height[i]时，需要找到左右的边界，

           Step 1: 因为使用单调栈做边界已确定，向右依次遍历，height[i] 的面积取决于第一个小于左边界的位置
           Step 2: 遍历完成后，栈内有其他元素， 说明 height[i] 的右边界即为自身（已找到），此时左侧元素为矩形的左边界

           边界条件: 遍历完后栈内还有其他元素，即右侧没有更小的元素存在，右边界固定，此时依次出栈判断左侧的边界

            解决方法： heights 前后放入,  哨兵 Sentinel，元素 0，
            - 最左侧的哨兵比所有元素都要小，永远不会出栈
            - 最右侧的哨兵会让所有元素出出栈

            特别注意：step 2 计算面积使用 stack[-1] 找出前一最小的元素
    """
        max_area, stack = 0, []
        heights = [0] + heights + [0]  # 前后加哨兵元素

        for k, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:  # 元素大于栈顶元素
                max_stack_ids = stack.pop()
                cur_area = heights[max_stack_ids] * (k - stack[-1] - 1)  # 前一个索引已经pop 出栈了, 此时stack[-1] 为前一个元素
                max_area = max(max_area, cur_area)  # 不算两边只取 中间的距离
            stack.append(k)
        return max_area


if __name__ == '__main__':
    nums = [2, 1, 5, 6, 2, 3]
    # nums = [2, 1, 2]  # [0, 2, 1, 2, 0]
    # [0, 1, 2]

    rst = Solution().largestRectangleArea(nums)
    print("result is", rst)
