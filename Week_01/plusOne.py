#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。
链接：https://leetcode-cn.com/problems/plus-one
示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        思路：
        1。 逢 9 进 1，
        2。若首位为 0，位数增加 1
        """

        # 倒序循环
        digits = [0] + digits
        for s in range(len(digits) - 1, -1, -1):
            if digits[s] != 9:
                digits[s] = digits[s] + 1
                break
            else:
                digits[s] = 0

        if not digits[0]:
            digits = digits[1:]
        return digits


if __name__ == '__main__':
    # digits = [1, 1, 2]
    digits = [9, 9, 9]
    rst = Solution().plusOne(digits)
    print("result is", rst)