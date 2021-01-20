#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个链表，判断链表中是否有环。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        思路：快慢指针
        快指针每次移动两次，慢指针移动一次
        判断条件：
            1。如果快慢指针相同则说明存在环
            2。快指针遇到 None， 说明没有环
        """
        if not head:
            return False

        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast.val == slow.val:
                return True
        return False

