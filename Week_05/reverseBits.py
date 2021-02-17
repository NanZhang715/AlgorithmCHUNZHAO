#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
颠倒给定的 32 位无符号整数的二进制位。

示例 1：

    输入: 00000010100101000001111010011100
    输出: 00111001011110000010100101000000
    解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
         因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。

链接：https://leetcode-cn.com/problems/reverse-bits
"""


class Solution:
    def reverseBits(self, n):
        """
        思路：
            n >> 1, 右移一位
            n & 1, 得到最左边位， 1 & 1 = 1， 1 & 0 = 0
        （1）n & 1 => 最后一位
        """
        rst, power = 0, 31
        while n:
            rst += (n & 1) << power
            n = n >> 1
            power -= 1
        return rst
