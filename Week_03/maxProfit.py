#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例：
    输入: [7,1,5,3,6,4]
    输出: 7
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        思路： 贪心，只要有盈利就进行交易

        交易策略：
        （1）单独交易日：今天买入，明天卖出，profit > 0, 就进行交易
        （2）连续上涨交易日， 第一天买入，最后一天卖出， 等价与每天都买卖
        （3）连续下降交易日， 不进行交易

        """
        profit, total_profit = 0, 0
        for s in range(1, len(prices)):
            profit = prices[s] - prices[s - 1]
            if profit > 0:
                total_profit += profit
        return total_profit


if __name__ == '__main__':
    # prices = [7, 1, 5, 3, 6, 4]
    prices = [1, 2, 3, 4, 5, 6]
    rst = Solution().maxProfit(prices)
    print("result is", rst)
