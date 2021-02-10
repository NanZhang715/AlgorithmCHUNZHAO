#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manacher算法 解决最长回文子串

- 定义
    A palindrome is a string that reads the same backward or forwards.
    For example, madam or racecar are some famous palindromic strings.

- 优点
    暴力法 O(n^3), DP O(n^2), 而 Manacher 将复杂度降低到 O(n)

- Intuition

情景 1 ：
    对于 "cacac"，第二个行表示如果以 s[i] 为中心，左右对称字符的数量

      c   a   c   a  c
      0   1   2   👆

    可以说 两个 a 互为镜像， 两个 c 互为镜像

情景 2：
      b  a [ c  a  c  a  c] d  e
      0  0  1   2  2  👆

    此时 a 并不互为镜像， 因为 a 超过了 cacac 的覆盖范围，但是 以 a 为中心的一部分回文在范围内

流程：
    1。 前提假设 字符串为奇数
    2。 s 中间加入 #， refered as  LPS
    3。 C 表示当前中心 ，R 表示以 C 为中心回文的范围， 半径需要将自身也算进去
    4。 递归整个 s， 数组的最大值就是 最长回文串的长度
"""


class Solution:
    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]
        # return P


if __name__ == '__main__':
    s = "aaab"
    rst = Solution().longestPalindrome(s)
    print("result is", rst)
