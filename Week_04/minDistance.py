#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
    你可以对一个单词进行如下三种操作：
     - 插入一个字符
     - 删除一个字符
     - 替换一个字符
示例 1：

    输入：word1 = "horse", word2 = "ros"
    输出：3
    解释：
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')
链接：https://leetcode-cn.com/problems/edit-distance/
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:



        return


if __name__ == '__main__':
    word1, word2 = "horse", "ros"
    rst = Solution().minDistance(word1, word2)
    print("result is", rst)

