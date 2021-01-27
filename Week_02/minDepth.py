#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树，找出其最小深度。、
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)

    if not left: return right + 1
    if not right: return left + 1
    return min(left, right) + 1
