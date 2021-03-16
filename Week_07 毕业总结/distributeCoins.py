#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
979. 在二叉树中分配硬币

给定一个有 N 个结点的二叉树的根结点 root，树中的每个结点上都对应有 node.val 枚硬币，并且总共有 N 枚硬币。
在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点)。
返回使每个结点上只有一枚硬币所需的移动次数。
"""


class Solution(object):
    def distributeCoins(self, root):
        """
        思路：
            若子节点为 0， 它所需的 1， 过载量为 -1
            若子节点为 3 ，过载量为 2， 需要将 2 个金币移出去
            过载量 math.abs(num_coin) - 1

            dfs 这个节点返回该节点的过载量
            node.val + dfs(node.left) + dfs(node.right) - 1。
        """
        self.ans = 0
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        left, right = self.dfs(node.left), self.dfs(node.right)
        self.ans += abs(left) + abs(right)
        return node.val + left + right - 1