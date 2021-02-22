#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~ 2h 个节点。

链接：https://leetcode-cn.com/problems/count-complete-tree-nodes/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """
        思路： 二分查找
               1        ----- level 1
             /   \
            2      3    ----- level 2
           / \    /
          4   5   6     ----- level 3

        背景知识
            (1) 完全二叉树节点树，最后一层节点索引范围 (2^(n-1), (2^n) - 1]
            (2) 判断 二叉树 index 节点是否存在
                - index 的二进制 "0" - 左子树， "1" 右子树
                - 通过位运算得到第 k 个节点的路径
                例如 6 -> "110", 排除最高位 "1"吗 7 的路径为 "10"

        时间复杂度：O(logn**2),二分需要 logn 步查找， 每次判断logn
        空间复杂度：O(1)

        """
        depth = self.get_depth(root)

        if depth < 2:
            return depth

        left, right = 2 ** (depth - 1), 2 ** depth - 1

        while left < right:
            mid = left + (right - left + 1) // 2  # 向上取整
            print(left, mid, right)
            if self.is_valid(mid, root):
                left = mid
            else:
                right = mid - 1

        return left

    def get_depth(self, root):

        depth = 0
        while root:
            root = root.left
            depth += 1
        return depth

    def is_valid(self, index, root):

        for s in bin(index)[3:]:
            if s == "1":
                root = root.right
            else:
                root = root.left
        return isinstance(root, TreeNode)


if __name__ == '__main__':
    # root = [1, 2, 3, 4, 5, 6]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)

    # print("depth is", Solution().get_depth(root))
    print("index 5 is", Solution().is_valid(5, root))
    print("result is", Solution().countNodes(root))
