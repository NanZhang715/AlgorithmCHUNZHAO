#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：
    输入："Let's take LeetCode contest"
    输出："s'teL ekat edoCteeL tsetnoc"

链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
"""


class Solution:
    def reverseWords(self, s: str) -> str:

        char_list = [self.reverse(char) for char in s.split(" ")]

        return " ".join(char_list)

    def reverse(self, char):

        if not char:
            return ""

        rst = []
        for s in char:
            rst.insert(0, s)
        return "".join(rst)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    rst = Solution().reverseWords(s)
    print("result is", rst)
