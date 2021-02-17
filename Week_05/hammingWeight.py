#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），
返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

示例 1：
    输入：00000000000000000000000000001011
    输出：3
    解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

链接：https://leetcode-cn.com/problems/number-of-1-bits
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        思路：位运算
            n & (n-1) 消除最后一个 1

        """

        count = 0
        while n:
            n = n&(n-1)
            count += 1
        return count


if __name__ == '__main__':
    n = 9
    rst = Solution().hammingWeight(n)
    print("result is", rst)