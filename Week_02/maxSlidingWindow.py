#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

链接：https://leetcode-cn.com/problems/sliding-window-maximum
"""
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        思路：两种方法，单调 stack 和 heap 都可以解决次 问题，
        stack 或者 heap 中都放入 元素索引， 遍历同时依次判断最大值是否在窗口内，
        如果在 输出 max， 如果不在依次 pop 直到 max 在窗口中

        1。 stack
        2。 heap

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        




        return
