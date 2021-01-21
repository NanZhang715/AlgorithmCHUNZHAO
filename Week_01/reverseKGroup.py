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
        思路: 每次反转 sub_list, 记录 head, tail, 结束后与前一个段连接
        """
        if k < 2 or not head:
            return head

        prev, cur = None, head
        while True:
            last_node_prev = prev  # 前一段的的最后一个 node
            last_node_sub = cur  # 当前 sublist 的 cur 反转后成为最后一个 node

            if not self.check_length(cur, k):  # 判断接下来的链表是否满足反转的条件
                break

            tmp, count = None, 0  # 创建两个临时变量
            while cur and count < k:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                count += 1

            # 连接前一段链表
            if last_node_prev:
                last_node_prev.next = prev
            else:
                head = prev

            # 连接后一段链表
            last_node_sub.next = cur

            # if not cur: break
            prev = last_node_sub
        return head

    def check_length(self, head, k):
        """
        判断 链表长度是否 大于 k
        """
        while head and k - 1:
            head = head.next
            k -= 1
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
