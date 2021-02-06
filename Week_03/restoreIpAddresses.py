#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

链接：https://leetcode-cn.com/problems/restore-ip-addresses/
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        """
        思路： dfs + 剪枝

        主函数：
            1。 path 每次递归放入整数
            2。 最终合法的 path 放入result 中

        dfs:
            1. 终止条件: 字符串被用完， 结果数据等于 4
            2. level task: 取 1 - 3 位数字
            3. 返回值：符合与要求的 path， 放入 result 中

        剪枝：
            1. 不能包含前导 0, 必须是整数
            2. 0 ～ 255 之间
            3. 长度 大于 4 段的 终止递归

        dfs的 复杂度
        时间复杂度：O(3^4), 每一段位数不超过 3，
        空间复杂度：O(n), IP  地址只有 4 个segment，递归栈的深度为 O(4)

        """
        if not s or len(s) < 4 or len(s) > 12:
            return []

        path, result = [], []
        self.dfs(s, path, result)
        return result

    def dfs(self, s, path, result):

        if len(s) > (4 - len(path)) * 3:
            return

        if not s and len(path) == 4:
            result.append('.'.join(path))
            return

        for i in range(min(3, len(s))): # s 的长度一直减少
            cur = s[:i+1]
            if (len(cur) > 1 and cur[0] == "0") or int(cur) > 255:
                continue
            self.dfs(s[i+1:], path + [s[:i+1]], result)


if __name__ == '__main__':

    print("result is", Solution().restoreIpAddresses("25525511135"))
    print("result is", Solution().restoreIpAddresses("1111"))