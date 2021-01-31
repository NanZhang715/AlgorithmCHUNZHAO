#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实现 pow(x, n)，即计算 x 的 n 次幂函数（即，xn）。
示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000

链接：https://leetcode-cn.com/problems/powx-n
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        """
        思路： 递归, 类似二分治
            时间复杂度：O(logn), 递归的层数
            空间复杂度：O(logn)

            - 负数，(1/x)^n
            - 偶数， x^(n/2) * x^(n/2)
            - 奇数， x* x^2
        """
        if not n:
            return 1.0
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

    def myPow_iter(self, x, n):

        """
        思路：利用迭代优化空间复杂度
        位运算：
            - 边界条件 x<=0, n =0
            - n < 0 时跳出循环
            - 当 x 为奇数时 乘以 x= rst*x, n-1, 位运算 n&1 ，判断 n 的二进制个位是否为 1
            - 当 x 为偶数时， x = x*x, n//2, n >> 1, 二进制删除一位
        """
        if x == 0.0:
            return 0.0
        rst = 1
        if n < 0:
            x, n = 1/x, -n
        while n:
            if n & 1:
                rst *= x
            x *= x
            n >>= 1  # 相当于 n = n/2
        return rst


if __name__ == '__main__':
    result = Solution().myPow(0.00001, 2147483647)
    # result = Solution().myPow_iter(2, 10)
    print(result)

