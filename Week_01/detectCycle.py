#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null

链接：https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        思路：快慢指针变形，增加一个指针
            1。快慢指针相遇在 环内 某一点
            2。此时 新的一个指针 和 slow 指针同时遍历，即可相遇在环的起点

        数学证明：
            设：a 为环外长度， b 为环内前半部分 ，c 为环内后半部分
            快慢指针相遇时：
            a + (n+1)b +nc = 2(a+b)
            => a = c + (n-1)(b+c)
        """
        fast, slow, ptr = head, head, head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        while slow != ptr:
            slow, ptr = slow.next, ptr.next
        return ptr
