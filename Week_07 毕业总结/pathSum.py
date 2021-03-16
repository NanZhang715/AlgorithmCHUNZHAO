#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
113. 路径总和 II

给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。

链接： https://leetcode-cn.com/problems/path-sum-ii/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        path, rst = [], []

        self.dfs(root, targetSum, path, rst)
        return rst

    def dfs(self, root, targetSum, path, rst):

        # None 返回
        if not root:
            return

        # 在根节点进行判断
        if not root.left and not root.right and targetSum == root.val:
            rst.append(path)
            return

        self.dfs(root.left, targetSum - root.val, path + [root.val], rst)
        self.dfs(root.right, targetSum - root.val, path + [root.val], rst)