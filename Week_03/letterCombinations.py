#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

例 1：
    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        return