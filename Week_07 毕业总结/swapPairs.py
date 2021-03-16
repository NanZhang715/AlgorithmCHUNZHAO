#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a linked list, swap every two adjacent nodes and return its head.

链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs/
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
    def swapPairs_recur(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        # 每 一 level有三个值，head，head.next, self.swapPairs(head.next.next)
        new_head = head.next
        head.next, new_head.next = self.swapPairs(new_head.next), head
        return new_head

    def swapPairs(self, head: ListNode) -> ListNode:

        """
        before:
            prev -> a -> b -> b.next
        After:
            prev -> b -> a -> b.next
        """

        if not head or not head.next:
            return head

        dummy = prev = ListNode(0)
        prev.next = head

        while prev.next and prev.next.next:
            a = prev.next  # cur 指针
            b = a.next  # 记录第三个 node位置
            prev.next, b.next, a.next = b, a, b.next
            prev = a  # 最后移动 prev 指针
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    rst = Solution().swapPairs(head)
    print(f"result of reverse is {rst.print_list()}")
