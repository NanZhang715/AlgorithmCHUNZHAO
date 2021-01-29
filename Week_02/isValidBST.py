#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

链接：https://leetcode-cn.com/problems/validate-binary-search-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        思路： 中序遍历为递增序列
        （1） 递归
                时间复杂度 O(n)
                空间复杂度 O(logn)，最差情况 O(n)， 递归栈的深度
        （2） 非递归, 优化方向，不用存储全部序列，仅保留上一个值，进行对比
                时间复杂度 O(n)
                空间复杂度 O(1)
        """
        prev, stack = float("-inf"), []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                # rst.append(node.val)
                if node.val <= prev:
                    return False
                prev = node.val
                root = node.right
        return True


if __name__ == '__main__':

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    rst = Solution().isValidBST(root)
    print("result is", rst)

