#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
721. 账户合并
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，
其余元素是 emails 表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，
它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按字符 ASCII 顺序排列的邮箱地址。账户本身可以以任意顺序返回。
"""
from typing import List
from collections import defaultdict

class DisjointUnionFindset:

    def __init__(self, n):
        self.parent = [s for s in range(n)]
        self.count = 0

    def find(self, s):
        """
        返回 u 的 parent 元素
        """
        if self.parent[s] == s:
            return s

        while self.parent[s] != s:
            self.parent[s] = self.parent[self.parent[s]]
            s = self.parent[s]
        return s

    def union(self, u, v):
        """
        合并 u, v
        """
        parent_u, parent_v = self.find(u), self.find(v)
        self.parent[parent_u] = parent_v
        self.count += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email_index, email_name = {}, {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_index:
                    email_index[email] = len(email_index)
                    email_name[email] = name

        disjoint = DisjointUnionFindset(len(email))

        for account in accounts:
            email_id = email_index[account[1]]
            for email in account[2:]:
                disjoint.union(email_id, email_index[email])

        index_email = defaultdict(list)
        for email, id in email_index.items():
            id = disjoint.find(id)
            index_email[id].append(email)

        rst = []
        for emails in index_email.values():
            rst.append([email_name[emails[0]]] + sorted(emails))
        print(email_index, email_name, index_email)
        return rst


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

    rst = Solution().accountsMerge(accounts)
    print("result is", rst)