#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。

请找出其中最小的元素。

示例 1：
    输入：nums = [3,4,5,1,2]
    输出：1

链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        思路：二分法变形, 以最小值为分界点 nums = l1 + l2, 最小值位于 l2 的首位
            target 取 nums[right]
                arr[mid] > target，  位于 l1 中， left = mid + 1
                arr[mid] < target,   位于 l2 中,  right 可能就是 最小值
                arrp[mid] == target, 不能确定答案, 就让右边界 减 1

            此方法也可以同时解决有重复数字出现的现象

          时间复杂度：O(logn)
          空间复杂度：O(1)
        """
        # 数组没有被旋转
        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:  # mid 在 l1 中
                left = mid + 1
            elif nums[mid] < nums[right]:  # 在 l2 中， 所以 mid 可能是最小点
                right = mid
            else:
                right -= 1  # 与右边界相同，不能确定右边界移动一位
        return nums[left]


if __name__ == '__main__':
    # nums = [3, 4, 5, 1, 2]
    nums = [3, 1, 2]
    # nums = [1, 5, 0, 0, 0]
    rst = Solution().findMin(nums)
    print("result is", rst)
