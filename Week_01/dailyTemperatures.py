#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
你的输出应该是   [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是[1, 30000]。每个气温的值的均为华氏度，都是在[30, 100]范围内的整数。
链接：https://leetcode-cn.com/problems/daily-temperatures
"""

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        思路：单调栈 其他 leetcode 例题包括 42, 739, 496, 316, 901, 402, 581
             和 柱状图最大矩形相似，不过单调栈应该使用 单调递减栈，stack 内放入元素索引
             遇到比栈顶大的元素，栈顶的元素对应的结果可以确定， 若比对顶元素小，则 push 入栈。
        边界条件：若遍历数组完后，stack 内的剩余元素对应的结果为 0， 即没有更高的温度出现

        时间复杂度 O(n)
        空间度复杂度 O(n)
        """
        n = len(T)
        stack, rst = [], [0] * n  # 创建辅助单调 stack， 以及与输入数组相同长度的数组作为输出

        for k, v in enumerate(T):
            while stack and v > T[stack[-1]]:  # 依次和 stack 内元素对比，找到之前元素的答案
                tmp = stack.pop()
                rst[tmp] = k - tmp
            stack.append(k)
        return rst


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    rst = Solution().dailyTemperatures(T)
    print("result is", rst)
