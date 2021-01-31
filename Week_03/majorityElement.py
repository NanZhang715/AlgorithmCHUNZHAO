#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于⌊n/2⌋的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：[3,2,3]
输出：3
链接：https://leetcode-cn.com/problems/majority-element
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        """
        Boyer-Moore
        时间复杂度：O(n) 对数组进行了一次遍历。
        空间复杂度：O(1) 常数级别的额外空间。
        """

        candidate, count = None, 0
        for s in nums:
            if not count:
                candidate = s
            else:
                if s == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate


if __name__ == '__main__':
    nums = [3, 2, 3]
    rst = Solution().majorityElement(nums)
    print("result is", rst)
