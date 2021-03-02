#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

链接：https://leetcode-cn.com/problems/sort-list
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        temp = self
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        """
        思路：归并

        三指针
            - fast 快指针，每次移动两步
            - slow 慢指针，每次移动一步
            - pre 慢指针的前继节点，用于截断 左右两部分的链表
        """

        if not head or not head.next:
            return head

        pre, fast, slow = None, head, head
        while fast and fast.next:  # 有一个条件不满足时
            pre, slow, fast = slow, slow.next, fast.next.next

        pre.next = None  # 截断链表

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.mergeList(left, right)

    def mergeList(self, left: ListNode, right: ListNode) -> ListNode:

        dummy = cur = ListNode(None)
        while left and right:
            if left.val <= right.val:
                cur.next, cur, left = left, left, left.next
            else:
                cur.next, cur, right = right, right, right.next

        # left and right at least one is None
        cur.next = left or right
        return dummy.next


if __name__ == '__main__':
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)
    rst = Solution().sortList(head)
    print("result is", rst.print_list())
