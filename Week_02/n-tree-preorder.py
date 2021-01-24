#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021/1/24 9:14 PM
@author: nzhang
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """
        思路： 和二叉树前序遍历相似，区别为 n 叉树有多个子节点， 入栈时使用 extend 方法
              而不是 append
        """

        if not root:
            return []
        stack, path = [root], []
        while stack:
            node = stack.pop()
            path.append(node.val)
            stack.extend(reversed(node.children))
        return path


