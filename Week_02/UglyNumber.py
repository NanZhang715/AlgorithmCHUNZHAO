#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。

说明:
1. 1 是丑数。
2. n 不超过1690
"""
import heapq


class Solution:
    def nthUglyNumber_heap(self, n: int) -> int:
        """
        背景知识 质因子例如 360 = 2*2*2*3*3*5 = 2^3 * 3^2 * 5
        丑数为 2^X * 3^Y* 5^Z

        思路 1 ：
         从 1 开始 依次 乘 2， 3， 5，递增 第n 个数为结果
         1。 用 heap 依次 pop 出下一个 质数， heap 的大小为 3， 需要 set 去重
         时间复杂度：O(n)
         空间复杂度：O(1) 维护了长度为 3 的 heap，以及 长度为丑数长度的 Set

        """
        heap, ugly_num, prev = [1], 1, set()

        # 每次循环都只 push 出一个元素
        for _ in range(n):
            while ugly_num in prev:
                ugly_num = heapq.heappop(heap)
            prev.add(ugly_num)
            for s in [2, 3, 5]:
                heapq.heappush(heap, ugly_num * s)
            print(ugly_num)
        return ugly_num

    def nthUglyNumber_dp(self, n: int) -> int:
        """
        思路
        2 ：动态规划 也可称做 三指针
        递推公式已知，可以用三个 指针分别表示 上一个丑数通过 乘 质因子的到的数字，
        下一个丑数为：
            min(p2*2, P3*3, P5*5)
        """
        dp = [1] * n
        p2, p3, p5 = 0, 0, 0  # 通项公式中 2， 3， 5 三个质数的指数
        for s in range(1, n):
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[s] = min(n2, n3, n5)
            if dp[s] == n2:
                p2 += 1
            if dp[s] == n3:
                p3 += 1
            if dp[s] == n5:
                p5 += 1
        return dp[-1]


if __name__ == '__main__':
    n = 10
    rst = Solution().nthUglyNumber_dp(n)
    print("result  is", rst)
