#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设 nums1 有足够的空间（空间大小等于 m + n）来保存 nums2
中的元素。

例 1：
    输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    输出：[1,2,2,3,5,6]

链接：https://leetcode-cn.com/problems/merge-sorted-array
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        思路：双指针
        依次从后向前遍历，依次取最大的放入 nums1 中
        """
        left, right = m - 1, n - 1
        p = len(nums1) - 1

        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[left], nums1[p] = nums1[p], nums1[left]
                left -= 1
            else:
                nums2[right], nums1[p] = nums1[p], nums2[right]
                right -= 1
            p -= 1

        # 如果 right < 0, 说明 nums2 的元素已经全部放入 nums1 中，即任务终止
        # 如果 right >=0 ,将 nums2 中任务元素 放入nums1相应位置即可
        if right >= 0:
            nums1[:right + 1] = nums2[:right + 1]

        return


if __name__ == '__main__':
    # nums1, m = [1, 2, 3, 0, 0, 0], 3
    # nums2, n = [2, 5, 6], 3
    nums1, m = [0], 0
    nums2, n = [1], 1
    Solution().merge(nums1, m, nums2, n)
    print("result is ", nums1)
