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

    def print_list(self):
        temp = self
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev, cur = None, head
#         while cur:
#             cur.next, prev, cur = prev, cur, cur.next
#         return prev

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    rst = Solution().reverseList(head)
    print(f"result of reverse is {rst.print_list()}")
