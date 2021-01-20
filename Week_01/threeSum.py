#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个包含 n 个整数的数nums，判断nums中是否存在三个元素 a，b，c ，
使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
链接：https://leetcode-cn.com/problems/3sum
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        思路： 排序 + 双指针
            1。 首先进行排序
            2。 初始化三个指针 k，  left， right, 即为 k < left < right
            3。 left ，right 夹逼 nums[left: right]
            4. 返回条件：
                1。 nums[left] > 0, 最小值大于 0， three sum  一定大于0
                2。 nunms[k] + nums[left] + nums[right] = 1, 返回结果
                3。 nunms[k] + nums[left] + nums[right] ！= 1， 跳过
            时间复杂度 O(nlogn 排序 + n^2 两层循环) => O(n^2)
            空间复杂度 O(1)
        """

        result = []
        if len(nums) < 3:
            return result

        nums.sort()
        for s in range(len(nums) - 2):
            left, right = s + 1, len(nums) - 1
            if nums[s] > 0:  # 第一项大于 0，直接 break
                break
            if s > 0 and nums[s] == nums[s - 1]:  # 若和前一个重复跳过
                continue

            while left < right:  # 三个数不能重复使用
                sum = nums[left] + nums[right] + nums[s]
                if sum == 0:
                    result.append([nums[s], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif sum < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum > 0:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result


if __name__ == '__main__':
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [-2, 0, 0, 2, 2]
    rst = Solution().threeSum(nums)
    print("result is", rst)
