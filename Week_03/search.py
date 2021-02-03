#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
33. 搜索旋转排序数组
升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        思路： 二分查找的变形， 数组在某个位置被旋转，所以会存在两个递增序列，

        1，  确定 递增区间 范围
            if nums[left] < nums[mid],  [left : mid] 是递增区间
            else  [mid：right] 是递增区间

        2，  通过 left， target， mid 进行比较，判断 target 是否在递增区间内
            if True，right = mid -1
            else, left = mid + 1， 排除【left， mid】 区间

        3，  正常二分法求找到 target 的位置

        时间复杂度 O(logn)：
        空间复杂福：O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[left]:  # 在前一个递增序列中
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 在第二个递增序列中
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    nums, target = [4, 5, 6, 7, 0, 1, 2], 0
    rst = Solution().search(nums, target)
    print("result is", rst)
