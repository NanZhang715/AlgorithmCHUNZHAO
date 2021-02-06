#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

例 1：
    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
"""
from typing import List


class Solution:

    def __init__(self):
        self.digit_dict = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        """
        思路：组合问题，使用 dfs, 每向下一层 digits少一位， 即 digits[1:]

        时间复杂度：O(3^m + 4^n), 3个字母的个数 m， 4个 字母的个数 n， 不同字母的组合数 3^m + 4^n
        空间复杂度：O(m+n),  递归调用层数最大 m + n
        """
        if not digits:
            return []

        n, path, result = len(digits), "", []
        self.dfs(digits, n, path, result)
        return result

    def dfs(self, digits, n, path, result):

        if len(path) == n:
            result.append(path)
            return

        for s in range(len(digits)):
            for letter in self.digit_dict[digits[s]]:
                self.dfs(digits[s+1:], n, path + letter, result)


if __name__ == '__main__':

    nums = "236"
    rst = Solution().letterCombinations(nums)
    print("result is ", rst)


