#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
链接： https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal1(self, root: TreeNode) -> List[int]:

        """
        思路： 递归
        1。 终止条件： root 为空
        2。 返回值 [root.val]
        3. level task: 左 + 根 + 右
        """

        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        思路：非递归, 使用辅助stack，push root.left 直到找到根节点 node，此时放入结果，
            使用 临时变量 为 tmp= node.right

        注意： 中序遍历的非递归必须熟练掌握，应为 bst 中序遍历的结果为递增序列， 很多变形可由此展开
        """
        stack, path = [], []

        while root or stack:  # root 和 stack 都为空时
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                path.append(node.val)
                root = node.right

        return path


    bin(2**2)
    bin(2**3)