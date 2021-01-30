#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。

示例 1:
    输入: [1,2,3]
        1
       / \
      2   3
    输出: 25
    解释:
    从根到叶子节点路径 1->2 代表数字 12.
    从根到叶子节点路径 1->3 代表数字 13.
    因此，数字总和 = 12 + 13 = 25.

链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        思路： dfs 保存 path，最终求和
        时间复杂度：O(n)，每个节点访问一次。
        空间复杂度：O(n)，空间复杂度主要取决于递归调用的栈空间，递归栈的深度等于二叉树的高度，最坏情况下为 O(n)
        """
        if not root:
            return 0

        path, result = root.val, []
        self.dfs(root, path, result)
        return sum(result)

    def dfs(self, root, path, result):

        # 如果递归到叶子节点，返回二叉树路径
        if not root.left and not root.right:
            result.append(path)
            return

        if root.left:
            self.dfs(root.left, path*10 + root.left.val, result)
        if root.right:
            self.dfs(root.right, path*10 + root.right.val, result)

    # def dfs(self, root, path_sum):
    #
    #     if not root:
    #         return 0
    #
    #     path_sum = 10 * path_sum + root.val
    #
    #     if not root.left and not root.right:
    #         return path_sum
    #
    #     return self.dfs(root.left, path_sum) + self.dfs(root.right, path_sum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print("Total Sum of Path Numbers: " + str(Solution().sumNumbers(root)))


if __name__ == '__main__':
    main()
