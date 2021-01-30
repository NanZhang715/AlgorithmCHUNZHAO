#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个 N 叉树，返回其节点值的后序遍历。

链接： https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        思路：后续 左 -> 右 -> 根

        使用一个栈来得到后序遍历。我们首先把根节点入栈。当每次我们从栈顶取出一个节点 u 时，
        就把 u 的所有子节点顺序推入栈中。例如 u 的子节点从左到右为 v1, v2, v3，
        那么推入栈的顺序应当为 v1, v2, v3，这样就保证了下一个遍历到的节点（即 u 的第一个子节点 v3）出现在栈顶的位置。
        在遍历结束之后，我们把遍历结果反转，就可以得到后序遍历。
        """
        if root is None:
            return []

        stack, path = [root], []
        while stack:
            root = stack.pop()
            if root:
                path.append(root.val)
            for c in root.children:
                stack.append(c)

        return path[::-1]