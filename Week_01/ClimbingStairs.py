#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""


class Solution:
    def climbStairs(self, n: int) -> int:

        """
        思路：f(n) = f(n-1) + f(n-2)
        初始条件： f(0) = 1, f(1) = 1，f(2) =2
        """

        if n < 2:
            return n

        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b

        return a
