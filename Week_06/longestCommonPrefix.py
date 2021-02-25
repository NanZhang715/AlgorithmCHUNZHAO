#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1：
    输入：strs = ["flower","flow","flight"]
    输出："fl"

链接：https://leetcode-cn.com/problems/longest-common-prefix/description/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        思路：纵向扫描

        时间复杂度：O(MN)
        空间复杂度：O(1)
        """
        if not strs:
            return ""
        strs.sort(key=lambda s: len(s))
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):  # any 只要有一个不满足
                return strs[0][:i]

        return strs[0]


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    rst = Solution().longestCommonPrefix(strs)
    print("result is", rst)
