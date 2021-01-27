#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
翻转一棵二叉树
链接：https://leetcode-cn.com/problems/invert-binary-tree/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        时间复杂度：O(N)，其中 NN 为二叉树节点的数目。我们会遍历二叉树中的每一个节点，对每个节点而言，我们在常数时间内交换其两棵子树。
        空间复杂度：O(N)。使用的空间由递归栈的深度决定，它等于当前节点在二叉树中的高度。在平均情况下，二叉树的高度与节点个数为对数关系，
        即 O(logN)。而在最坏情况下，树形成链状，空间复杂度为 O(N)。

        """
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.right = left
        root.left = right
        return root
