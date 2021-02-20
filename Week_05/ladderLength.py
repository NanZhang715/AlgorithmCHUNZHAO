#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
127. 单词接龙
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目。
如果不存在这样的转换序列，返回 0。


示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

注意：endWord.length == beginWord.length
链接：https://leetcode-cn.com/problems/word-ladder/
     https://leetcode.com/problems/word-ladder/discuss/346920/Python3-Breadth-first-search
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        """
        思路：bfs
             startword 和 endword 长度一致， 每次按位置替换 startword， 判断中间 word 是否在 wordlist 中

                     hit
               /      |      \
               *it   h*t   hi*

             wordList = ["hot","dot","dog","lot","log","cog"]
             word_dict ={ *ot : hot, dot, lot
                        h*t : hot
                        ho* :hot
                        d*t : dot
                        do* : dot, dog
                        *og : dog, log, cog
                        d*g : dog
                        l*t : lot
                        lo* : lot, log
                        l*g : log
                        c*g: cog
                        co* : cog}
        """

        if endWord not in wordList or not beginWord or not endWord or not wordList:

            return 0

        n, word_dict = len(beginWord), defaultdict(list)
        for word in wordList:
            for i in range(n):
                word_dict[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            cur_word, level = queue.popleft()
            for s in range(n):
                intermediate = cur_word[:s] + "*" + cur_word[s+1:]
                for word in word_dict[intermediate]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
        return 0


if __name__ == '__main__':

    beginWord, endWord, wordList = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    rst = Solution().ladderLength(beginWord, endWord, wordList)
    print("result is", rst)
