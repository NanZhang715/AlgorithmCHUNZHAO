#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        思路：
        根 -> 左 -> 右
        1。 递归方法和中序遍历相似

        2。 非递归方法，类似层序遍历，使用辅助 stack， 依次放入 [root.left, root.right]，依次遍历 stack 中的元素
            直到 stack 为空
        """

        path, stack = [], [root]
        if not root:
            return path

        # 因为 stack 先入后出的性质，所以先 push root.right, 再 push root.left
        while stack:
            root = stack.pop()
            path.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return path


        return path