#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明:叶子节点是指没有子节点的节点。

示例:
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
链接：https://leetcode-cn.com/problems/binary-tree-paths
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        """
        思路：dfs

        - 终止条件：遇到叶子节点将 path 放入 result 中，并返回
        - 返回 result
        - level task：path + 子节点

        时间复杂度：O(N^2)，其中 N 表示节点数目。在深度优先搜索中每个节点会被访问一次且只会被访问一次，
        每一次会对 path 变量进行拷贝构造，时间代价为 O(N)，故时间复杂度为 O(N^2)。

        空间复杂度：O(N^2)，出结果列表还要考虑递归栈的调用
        """

        if not root: return []

        path, result = str(root.val), []
        self.dfs(root, path, result)
        return result

    def dfs(self, root, path, result):

        # root 为叶子节点
        if not root.left and not root.right:
            result.append(path)
            return

        if root.left:
            self.dfs(root.left, path + "->" + str(root.left.val), result)
        if root.right:
            self.dfs(root.right, path + "->" + str(root.right.val), result)