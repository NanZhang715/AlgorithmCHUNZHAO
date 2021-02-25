#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，

而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。

链接：https://leetcode-cn.com/problems/number-of-provinces
查并集：https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/
"""

from typing import List


class DisjointSet:
    """
    并查集：
        - 数据结构与树类似，区别节点只记录 父节点，而树只记录子节点
        - Union 合并两个 single set
        - find 查询某个元素属于哪个集合，通常是返回集合内的一个“代表元素”。这个操作是为了判断两个元素是否在同一个集合之中。
    """

    def __init__(self, n):
        """
        初始化节点
        """
        self.parent = [s for s in range(n)]
        self.count = 0

    def find(self, s):
        """
        查找属于哪个集合，返回 parent 节点
        """
        if s == self.parent[s]:  # 如果本身就是根节点直接返回自身
            return s

        while s != self.parent[s]:
            # 路径压缩
            self.parent[s] = self.parent[self.parent[s]]
            s = self.parent[s]
        return s  # 返回父节点

    def union(self, u, v):
        """
        找到 u, v 的父节点，进行合并
        """
        parent_u, parent_v = self.find(u), self.find(v)
        self.parent[parent_u] = parent_v
        self.count -= 1

    def connected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        """
        思路： 并查集

        时间复杂度：O(N^2*logN), 遍历所有节点 N^2， 遇到相连 2次查找， 1次合并， 一共 2N^2查找， N^2合并
        空间复杂度：O(N)
        """

        if not isConnected:
            return 0

        n = len(isConnected)
        disjoint = DisjointSet(n)
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    disjoint.union(i, j)
        print(disjoint.parent)
        return sum(disjoint.parent[i] == i for i in range(n))


if __name__ == '__main__':
    # isConnected = [[1, 1, 0],
    #                [1, 1, 0],
    #                [0, 0, 1]]
    isConnected = [[1, 0, 0, 1],
                   [0, 1, 1, 0],
                   [0, 1, 1, 1],
                   [1, 0, 1, 1]]
    rst = Solution().findCircleNum(isConnected)
    print("result is", rst)
