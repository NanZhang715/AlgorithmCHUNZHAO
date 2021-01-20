#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a linked list, swap every two adjacent nodes and return its head.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        思路：递归
        1。 终止条件：head 后只有 一个 node，即 not head or  not head.next
        2.  每层 返回值： 已排好序的后两个 node 的 head
        3。 本 level 处理的 task，交换两个 node
        空间复杂度 O(n)
        """
        if not head or not head.next:
            return head

        # 每 一 level有三个值，head，head.next, self.swapPairs(head.next.next)
        new_head = head.next
        head.next, new_head.next = self.swapPairs(new_head.next), head
        return new_head

    def swapPairs(self, head: ListNode) -> ListNode:
        """
        思路：非递归
        1。 终止条件：head 后只有 一个 node，即 not head or not head.next
        2.  每次交换三个指针类似 链表 反转
        空间复杂度 O(1)
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


if __name__ == '__main__':

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    rst = Solution().swapPairs(head)
    print(f"result of reverse is {rst.print_list()}")
