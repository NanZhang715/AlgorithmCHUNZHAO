#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
机器人在一个无限大小的 XY 网格平面上行走，从点(0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：

-2 ：向左转 90 度
-1 ：向右转 90 度
1 <= x <= 9 ：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。

机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
返回从原点到机器人所有经过的路

注意：
    北表示 +Y 方向。
    东表示 +X 方向。
    南表示 -Y 方向。
    西表示 -X 方向。

示例 1：
    输入：commands = [4,-1,3], obstacles = []
    输出：25
    解释：
    机器人开始位于 (0, 0)：
    1. 向北移动 4 个单位，到达 (0, 4)
    2. 右转
    3. 向东移动 3 个单位，到达 (3, 4)
    距离原点最远的是 (3, 4) ，距离为 32 + 42 = 25

链接：https://leetcode-cn.com/problems/walking-robot-simulation
"""

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        """
        思路： 北:0， 东:1， 南:2， 西:3

        """

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, direct = 0, 0, 0
        obstacles = set(map(tuple, obstacles))  # list 转 set， [[1,2], [2, 4]] 转  ((1,2), (2, 4))
        rst = 0

        for s in commands:
            if s == -2:  # 向左
                direct = (direct + 3) % 4
            elif s == -1:  # 向右
                direct = (direct + 1) % 4
            else:
                for k in range(s):
                    if (x + dx[direct], y + dx[direct]) not in obstacles:
                        x += dx[direct]
                        y += dy[direct]
                        rst = max(rst, x * x + y * y)

        return rst


if __name__ == '__main__':
    command, obstacles = [4, -1, 4, -2, 4], [[2, 4]]
    rst = Solution().robotSim(command, obstacles)
    print("result is", rst)
