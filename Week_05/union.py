#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
并查集
"""


class union_find:
    def init(n):
        # for i = 0 .. n:
        p = [i for i in range(n)]

    def union(self, p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:  # 路径压缩 ?
            x = i;
            i = p[i];
            p[x] = root
        return root