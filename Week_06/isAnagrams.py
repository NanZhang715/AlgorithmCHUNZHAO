#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:

    输入: s = "rat", t = "car"
    输出: false
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        思路：哈希表分别扫描 s,t, 判断最终是否为空

        时间复杂：O(n)
        空间复杂：O(1)
        """
        count = [0] * 26
        for char in s:
            count[ord(char) - ord("a")] += 1

        for char in t:
            if count[ord(char) - ord("a")]:
                count[ord(char) - ord("a")] -= 1
            else:
                return False

        # any/all 对于一个可迭代的 对象
        return False if any(count) else True


if __name__ == '__main__':
    s, t = "anagram", "nagaram"
    rst = Solution().isAnagram(s, t)
    print("result is", rst)