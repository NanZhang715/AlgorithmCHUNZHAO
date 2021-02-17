#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
231. 2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
    输入: 1
    输出: true
    解释: 20 = 1
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        思路：2 的幂表示 n 的二进制只有一个 1,
        删除 1，判断是否等于 0
        """
        if not n:
            return False

        return n & (n - 1) == 0


if __name__ == '__main__':
    n = 7
    rst = Solution().isPowerOfTwo(n)
    print("result is", rst)
