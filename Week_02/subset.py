#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Statement
Given a set with distinct elements, find all of its distinct subsets.

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

时间复杂度 O(2^n)

"""


def find_subsets_bfs(nums):
    subsets = [[]]
    for s in nums:
        subsets += [cur + [s] for cur in subsets]
    return subsets


def find_subsets_lexi(nums):
    """
    Lexicographic (Binary Sorted) Subsets
    """
    subsets = []
    n = len(nums)
    for i in range(2**n, 2**(n+1)):
        bitmask = bin(i)[3:]  # generate bitmask, from 000 to 111
        # print(bitmask)

        subsets.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets_bfs([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets_lexi([1, 5, 3])))


if __name__ == '__main__':
    main()
