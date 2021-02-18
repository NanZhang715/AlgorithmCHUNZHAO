#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        """
        思路：

        Before:

        [ 1,  2]  ->      [3  ->  4] ->  [5,  6]
              |            |
            prev          cur
            prev_tail   sub_tail

        After:

        [ 1,  2 ] ->       [ 3  <-   4 ] ->  [5, 6]
              |             |       |         |
              |             |     prev       cur
            prev_tail   sub_tail

        """
        prev, cur = None, head

        while self.check_length(cur, k):

            first_tail, sub_tail = prev, cur

            for _ in range(k):
                cur.next, prev, cur = prev, cur, cur.next

            # 连接前一段
            if first_tail:
                first_tail.next = prev
            else:
                head = prev

            # 连接后一段
            sub_tail.next = cur

            prev = sub_tail

        return head

    def check_length(self, head, n):

        while head and n - 1:
            head = head.next
            n -= 1

        return isinstance(head, ListNode)


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = Solution().reverseKGroup(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


if __name__ == '__main__':
    main()
