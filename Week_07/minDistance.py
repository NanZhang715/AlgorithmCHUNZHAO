#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：

    - 插入一个字符
    - 删除一个字符
    - 替换一个字符

示例 1：
    输入：word1 = "horse", word2 = "ros"
输出：
    3
解释：
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
链接: https://leetcode-cn.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        思路：DP

        dp[i][j] 表示 word1 前 i 个字母 与 word2 前 j 个字母的编辑距离
        opt 方程：
        (1) when word1[i] == word2[j],
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] -1) + 1

        (2) when word1[i] != word2[j],
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                 #     r     o    s
            #    0     1     2    3
            h    1     1     2    3
            o    2     2     1    2
            r    3
            s    4
            e    5

            dp[i][0] = len(word1[:i])
            dp[0][j] = len(word1[:j])
         """
        m, n = len(word1) + 1, len(word2) + 1

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1) + 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[-1][-1]


if __name__ == '__main__':
    word1, word2 = "horse", "ros"
    rst = Solution().minDistance(word1, word2)
    print("result is", rst)
