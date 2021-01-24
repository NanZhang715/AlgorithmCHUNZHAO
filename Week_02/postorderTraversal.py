#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树，返回它的 后序 遍历。

连接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        """
        思路： 后续遍历  右 -> 左 -> 根
              可转换为  根 -> 左 -> 右 的逆序列，此时类似 中序遍历，
              最后将结果 reverse 即可
        """

        if not root:
            return []

        stack, path = [], []
        while stack or root:
            if root:
                stack.append(root)
                path.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        return path[::-1]
