#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
516. 最长回文子序列
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1:
输入:
    "bbbab"
输出:
    4

链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence/
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        思路： DP

        dp[i][j] 表示 s[i:j]中最长的回文子序列 dp[0][n-1] 即为答案

        dp[i][j] = dp[i+1][j-1] + 2

            b   b   b   a   b
        b   1   2   1
        b       1
        b           1
        a               1
        a                   1
        """
        if not s:
            return 0

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


if __name__ == '__main__':
    # s = "bbbab"
    s = "cbbd"
    rst = Solution().longestPalindromeSubseq(s)
    print("result is", rst)
    # for s in range(len(dp)):
    #     print(dp[s])
