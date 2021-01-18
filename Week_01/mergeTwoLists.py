#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
import heapq


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        思路：使用 min_heap, 依次 pop 出最小的 Node
        """
        min_heap = []
        for s in [l1, l2]:
            if s:
                heapq.heappush(min_heap, s)

        head, tail = None, None
        while min_heap:
            node = heapq.heappop(min_heap)
            if not head:
                head = tail = node
            else:
                tail.next = node
                tail = tail.next

            if node.next:
                heapq.heappush(min_heap, node.next)

        return head


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    result = Solution().mergeTwoLists(l1, l2)
    print("Here are the elements form the merged list: ", end='')
    while result:
        print(str(result.val) + " ", end='')
        result = result.next
