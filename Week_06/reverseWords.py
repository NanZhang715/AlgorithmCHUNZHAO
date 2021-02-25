#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。

说明：
    无空格字符构成一个 单词 。
    输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
    如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

示例 1：

    输入："the sky is blue"
    输出："blue is sky the"

链接：https://leetcode-cn.com/problems/reverse-words-in-a-string/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        思路：split string to list, 1) 反转str 2）反转 list

        时间复杂度 O(n)
        空间复杂度 O(n)
        """
        char_list = [char for char in s.split(" ") if char]
        self.reverse(char_list)
        return " ".join(char_list)

    def reverse(self, s):

        if not s:
            return ""

        left, right = 0, len(s) - 1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    # s = "the sky is blue"
    s = "  hello world  "
    rst = Solution().reverseWords(s)
    print("result is", rst)
