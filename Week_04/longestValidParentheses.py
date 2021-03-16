#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
    输入：s = ")()())"
    输出：4
    解释：最长有效括号子串是 "()()"

链接：https://leetcode-cn.com/problems/longest-valid-parentheses/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        思路：DP， dp[i]截止表示该位有效括号的数量, 左括号 dp[i] = 0

        有效括号，一定是 ")" 结尾
            1）前一个是 dp[i -1] 是 "(",
                    dp[i] = dp[i-2] + 2

            2）前一个是 dp[i-1] 是 ")"，
                    dp[i] = dp[i-1] + dp[i - dp[i−1]−2] + 2
                            前一位有效数 + 前一位有效数字 之前的数量 + 本身 2 位

            示例：对于第 dp[5] 个 ")", 结果为前一个 dp[4] 加 dp[0]

                )  (   )  (   )   )
                0  0   2  0   4   0

            时间复杂度：O(n)
            空间复杂度：O(n)
        """

        if not s or len(s) < 2:
            return 0

        dp = [0] * len(s)
        dp[1] = 2 if s[:2] == "()" else 0

        for i in range(2, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2

        return max(dp)


if __name__ == '__main__':

    s = ")()())"
    rst = Solution().longestValidParentheses(s)
    print("result is", rst)