#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
394. 字符串解码
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
    输入：s = "3[a]2[bc]"
    输出："aaabcbc"
示例 2：
    输入：s = "3[a2[c]]"
    输出："accaccacc"
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        思路： stack

            -  数字 字符转换成数字
            - "[" 栈内加入 当前 [count，rst], 然后分别 置于空
            - 字母 rst 尾部添加
            - "]" 出栈 之前的 prev_char + count * rst

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        rst, stack, count = "", [], 0

        for k in s:
            if k == '[':
                stack.append([count, rst])
                rst, count = "", 0
            elif k == ']':
                prev_count, prev_char = stack.pop()
                rst = prev_char + prev_count * rst
            elif k.isdigit():
                count = count * 10 + int(k)  # case for nums >= 10
            elif k.isalpha():
                rst += k
            print(rst, stack, count)
        return rst


if __name__ == '__main__':
    s = "3[a]2[bc]"
    # s = "3[a2[c]]"
    rst = Solution().decodeString(s)
    print("result is", rst)
