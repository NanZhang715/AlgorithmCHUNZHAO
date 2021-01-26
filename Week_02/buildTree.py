#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]

链接： https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        思路： 递归的方法 build  tree
        前序 List， 第一个为 root
        中序 List中，小于 root 为 root.left, 大于 root 为 root.right
        即
        preorder = [root] + [left] + [right]
        inorder = [left] + [root] + [right]

        时间复杂度：O(n), 依次遍历 n， n/2，..., 1, O(2n)
        空间复杂度：O(n)
        """
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        root_idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])

        return root
