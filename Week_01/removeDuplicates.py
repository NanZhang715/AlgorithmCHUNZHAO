#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。不要使用额外的数组空间，
你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array

示例 1:
    给定数组 nums = [1,1,2], 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
    你不需要考虑数组中超出新长度后面的元素。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        思路： 双指针， 因为是有序数组，相同元素相邻nums, left 指向最后一个不重复元素， right 指向下一个不重复元素位置
        nums[left], nums[right] 元素不同， 交换 nums[right] , nums[left +1]
        最终左指针的位置 + 1 即为数组新的长度
        """
        left, right = 0, 0
        while right < len(nums):
            if nums[left] != nums[right]:
                nums[left + 1], nums[right] = nums[right], nums[left + 1]
                left += 1
            right += 1
        return left + 1  # 最终数组长度为 left + 1


if __name__ == '__main__':
    arr = [1, 1, 2]
    rst = Solution().removeDuplicates(arr)
    print("result is", rst)
