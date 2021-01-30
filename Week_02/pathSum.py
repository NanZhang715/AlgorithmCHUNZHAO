#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

链接：https://leetcode-cn.com/problems/path-sum-ii
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        """
        思路： dfs，sum 每次减去节点值，到叶子节点时 sum == leaf.val, 返回 path

        时间复杂度：O(N^2) 其中 N 是树的节点数。在最坏情况下，树的上半部分为链状，下半部分为完全二叉树，
        并且从根节点到每一个叶子节点的路径都符合题目要求。此时，路径的数目为 O(N)，
        并且每一条路径的节点个数也为 O(N)，因此要将这些路径全部添加进答案中，时间复杂度为 O(N^2)。

        空间复杂度：O(N)，其中 NN 是树的节点数。空间复杂度主要取决于栈空间的开销，栈中的元素个数不会超过树的节点数。
        """

        if not root: return []

        path, result = [root.val], []
        self.dfs(root, targetSum, path, result)
        return result

    def dfs(self, root, targetSum, path, result):

        if not root.left and not root.right and root.val == targetSum:
            result.append(path)
            return

        if root.left:
            self.dfs(root.left, targetSum - root.val, path + [root.left.val], result)
        if root.right:
            self.dfs(root.right, targetSum - root.val, path + [root.right.val], result)


