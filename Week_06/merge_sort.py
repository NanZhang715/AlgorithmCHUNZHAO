#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
归并排序
"""


def merge_sort(nums):

    if len(nums) < 2:
        return nums

    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result += left
    if right:
        result += right

    return result


if __name__ == '__main__':

    nums = [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
    arr_new = merge_sort(nums)
    print("归并排序结果：", arr_new)
