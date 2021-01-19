#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

链接：https://leetcode-cn.com/problems/group-anagrams
"""

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        思路：计数法
        用一个 26位数字表示 str，判断是否为异位字符串
        注意：
            1。 字典的值 必须转成  tuple， 才可以hash， 作为字典的 key
            2。 defaultdict 可初始化默认的 List，可以使用 List append的方法
        """
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            ans[tuple(count)].append(s)
        return list(ans.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    rst = Solution().groupAnagrams(strs)
    print("result is", rst)
