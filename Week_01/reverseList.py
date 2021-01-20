#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reverse a singly linked list.

https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
