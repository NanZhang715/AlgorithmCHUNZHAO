#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
91. 解码方法
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。
例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。
注意，"06" 不能映射为 "F" ，因为 "6" 和 "06" 不同。
给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。


示例 1：

输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2：
"""


class Solution:
    def numDecodings(self, s: str) -> int:

        """
        思路： 动态规划,  与剑指 offer类似，但有区别：
        如果 前 i个字符不能结果, 则整个字符都不能被解码

        dp[n] 为截止到 n,可以翻译的数量
        如果 2 位数字可以被翻译 f(n-2), 如果一位数字可以被翻译 f(n-1)
        如果 1 位 和两位都可以被翻译

            f(n) = f(n-1) + f(n-1)
            f(0)= 1 , f(1) = 1, f(2) = 2

         条件：
            1。[1,26] 之间的数字可以翻译
            2。首位为 0 的数组，不可被翻译

         时间复杂度：O(n)
         空间复杂度：O(n)
        """

        if not s or s[0] == "0":
            return 0

        dp = [0 for _ in range(len(s) + 1)]

        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        for k in range(2, len(s) + 1):

            if 0 < int(s[k-1:k]) <= 9:
                dp[k] += dp[k-1]
            if 10 <= int(s[k-2:k]) <= 26:
                dp[k] += dp[k-2]
        return dp[-1], dp


if __name__ == '__main__':
    # s = "12"
    s = "2101"
    rst = Solution().numDecodings(s)
    print("result is", rst)



