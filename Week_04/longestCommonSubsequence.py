#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1143. 最长公共子序列
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符
（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

示例 1:

    输入：text1 = "abcde", text2 = "ace"
    输出：3
    解释：最长公共子序列是 "ace"，它的长度为 3。

链接：https://leetcode-cn.com/problems/longest-common-subsequence/
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        思路： DP

        dp[i][j] 表示 text1 前 i 位, text2 前 j 位，相同的字符数

             ""  a   b   c   d   e
         ""     0    0
         a      1    0   0   0   0
         c      1    1   2   2   2
         e      1    1   2   2   3

         dp[i][j] = dp[i-1][j-1] + 1
         dp[i][j] = max(dp[i-1][j], dp[i][j-1])

            时间复杂度：O(mn)
            空间复杂度：O(mn)
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    text1, text2 = "abcde", "ace"
    rst = Solution().longestCommonSubsequence(text1, text2)
    print("result is", rst)

