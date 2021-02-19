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

from collections import defaultdict


class DisjointSet:
    """
    并查集：
        - 数据结构与树类似，区别节点只记录 父节点，而树只记录子节点
        - Union 合并两个 single set
        - find 查询某个元素属于哪个集合，通常是返回集合内的一个“代表元素”。这个操作是为了判断两个元素是否在同一个集合之中。
        - add 添加一个新集合，其中有一个新元素。添加操作不如查询和合并操作重要，常常被忽略。
    """

    def __init__(self, n):
        """
        初始化节点
        """
        self.parent = [s for s in range(n)]

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

    def connected(self, u, v):
        return self.find(u) == self.find(v)


if __name__ == '__main__':

    isConnected = [[1, 1, 0],
                   [1, 1, 0],
                   [0, 0, 1]]
    n = len(isConnected)
    disjoint = DisjointSet(n)
    for i in range(n):
        for j in range(i, n):
            if isConnected[i][j] == 1:
                disjoint.union(i, j)










