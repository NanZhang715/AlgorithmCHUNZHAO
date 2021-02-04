#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如 sqrt。

示例 1：
    输入：16
    输出：True
    示例 2：

    输入：14
    输出：False
链接：https://leetcode-cn.com/problems/valid-perfect-square
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        思路： 牛顿法， 与 int 求 root_square 相似
        判断 结果是否为整数
        """
        if num == 1: return True
        s = num // 2
        while s * s > num:
            s = (s + num / s) // 2
        return s * s == num


if __name__ == '__main__':
    result = Solution().isPerfectSquare(num=14)
    print(result)
