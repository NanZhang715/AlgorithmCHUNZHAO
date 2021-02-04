#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

    输入: 4
    输出: 2
    示例 2:

    输入: 8
    输出: 2
    说明: 8 的平方根是 2.82842...,
        由于返回类型是整数，小数部分将被舍去。

链接：https://leetcode-cn.com/problems/sqrtx
"""


class Solution:
    def mySqrt(self, num: int) -> int:

        """
        思路: 牛顿法
        即需要求 x^2 - num = 0 时， x 的值
        设 f(x) = x^2 - num, f'(x) = 2x

          类似梯度下降
            x = x - f/f' = x - （x^2 - num）/ 2x = x - x/2 + num/2x = (x + num/x)/2
          即 x = (x + num/x)/2

         时间复杂度：O(logn)
         空间复杂地：O(1)
        """
        if num < 2:
            return num

        s = x // 2  # 从 1/2 处开始查找
        while s * s > x:
            s = (s + num / s) // 2
        return int(num)


if __name__ == '__main__':
    x = 8
    rst = Solution().mySqrt(x)
    print("result is ", rst)
