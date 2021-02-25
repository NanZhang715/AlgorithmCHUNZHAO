#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。

示例 1:

    输入:
        s: "cbaebabacd" p: "abc"

    输出:
        [0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        思路： 滑动窗口遍历 s， 利用哈希表进行异位词的判断
        """
        char_dict, rst, n = {}, [], len(p)

        # 构建哈希表
        for char in p:
            char_dict[char] = char_dict.get(char, 0) + 1

        print(char_dict)

        start = 0
        for end, char in enumerate(s):
            if char in char_dict:
                char_dict[char] -= 1

            if end + 1 > n:
                if s[start] in char_dict:
                    char_dict[s[start]] += 1
                start += 1

            # 判断 char_dict 的 value 是否全为 0
            if not any(char_dict.values()):
                rst.append(start)

        return rst


if __name__ == '__main__':
    s, p = "cbaebabacd", "abc"
    rst = Solution().findAnagrams(s, p)
    print("result is", rst)
