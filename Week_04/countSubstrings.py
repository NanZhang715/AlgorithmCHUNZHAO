#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

    输入："aaa"
    输出：6
    解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

链接：https://leetcode-cn.com/problems/palindromic-substrings/
"""


class Solution:
    def countSubstrings_dp(self, s: str) -> int:
        """
        思路： 动态规划， 回文子串的数量，类似的有最长回文子串

        dp[i][j] 表示 i 开始至 j 位是否是回文
        dp[i][j] = dp[i+1][j-1] and dp[i] == dp[j]， count +=1
        边界条件: 对角线元素为回文，只需要计算上半个矩阵，结果为 dp[-1][-1]

              a   a   a

        a     1   2   6
        a         1   2
        a             1

        时间复杂度：O(n^2)
        空间复杂度：O(n^2)

        使用 Manacher 算法可以将 空间复杂度可以优化到 O(n)
        """
        n, count = len(s), 0
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
                    count += 1
                elif j - i + 1 == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                elif j - i + 1 > 2 and s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    count += 1

        return count

    def countSubstrings_pivot(self, s: str) -> int:

        """
        思路： 可以使用中心扩展法，将空间复杂度降为 O(1)
              - 奇数回文 从一个中心点扩散
              - 偶数回文 中心点为 两个字符
              - 以单个字符以及相邻两个字符进行左右拓展，获得所有可能的回文字符串。

        时间复杂度：O(n^2)
        空间复杂度：O(1)

        """
        n, count = len(s), 0

        for i in range(n):
            count += self.expand(s, i, i)
            count += self.expand(s, i, i + 1)
        return count

    def expand(self, s, left, right):

        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1
        return count

    def manacher(self, s: str) -> int:
        """

        思路： Manacher 算法可以将时间复杂度将为 O(n)
            http://manacher-viz.s3-website-us-east-1.amazonaws.com
        """

        return


if __name__ == '__main__':
    s = "aaa"
    rst = Solution().countSubstrings_pivot(s)
    print("result is", rst)
