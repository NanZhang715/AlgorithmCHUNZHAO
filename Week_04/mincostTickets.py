#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
983. 最低票价
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。
每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，
那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。
"""
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        思路： DP

        dp[i] 表示从 第 i 天到最后一天的最小花费
        - 第 i 天不旅行，dp(i) = dp(i - 1)
        - 第 i 天旅行，dp(i) = min(dp(i + j) + cost(j))  j -> [1, 7, 30]

        dp(i) = min(dp(max(i-1, 0)) + cost[0],
                    dp(max(i- 7, 0)) + cost[1],
                    dp(max(i- 30, 0)) + cost[2])
        时间复杂度：O(days[-1])
        空间复杂度：O(day[-1])
        """
        dp = [0] * (days[-1] + 1)
        for s in range(1, len(dp)):
            if s not in set(days):
                dp[s] = dp[s-1]
            else:
                dp[s] = min(dp[max(0, s - 1)] + costs[0],
                            dp[max(0, s - 7)] + costs[1],
                            dp[max(0, s - 30)] + costs[2])

        return dp[-1]


if __name__ == '__main__':

    days, costs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]
    rst = Solution().mincostTickets(days, costs)
    print("resultr is", rst)