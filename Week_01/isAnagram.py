#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
链接：https://leetcode-cn.com/problems/valid-anagram/description/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """
        思路：
        用一个字典保存字符串出现的次数 {"string": count}，以下情况返回 False
        1。 字符串 count  小于 0
        2。 t 中字符不存在 字典中
        3。 最终 字典存在 count 大于 0 的item
        """
        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1

        for char in t:
            if char in char_dict:
                char_dict[char] -= 1
                if char_dict[char] == 0:
                    del char_dict[char]
            else:
                return False

        if not char_dict:
            return True
        else:
            return False


if __name__ == '__main__':
    s, t = "anagram", "nagaram"
    rst = Solution().isAnagram(s, t)
    print("result is", rst)

