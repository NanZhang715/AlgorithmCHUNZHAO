#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true，否则返回 false。

示例 1：
    输入：[5,5,5,10,20]
    输出：true
    解释：
    前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
    第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
    第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
    由于所有客户都得到了正确的找零，所以我们输出 true。

链接：https://leetcode-cn.com/problems/lemonade-change

"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        思路： 贪心，一共有三种面值， 5， 10， 20
        收到 10 时， 5 的数量减一， 10 的数量增加
        收到 20 时， 有两种找法：（1） 5 + 10， （2）3 张 5 元,  优先使用第一种方案

        时间复杂度: O(n)
        空间复杂度: O(1)

        """

        five, ten = 0, 0
        for s in bills:
            if s == 5:
                five += 1
            elif s == 10:
                five, ten = five - 1, ten + 1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            if five < 0: return False
        return True


if __name__ == '__main__':
    bills = [5, 5, 5, 10, 20]
    rst = Solution().lemonadeChange(bills)
    print("result is", rst)