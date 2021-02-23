#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快排
"""


def quick_sort(nums, beg, end):
    if beg < end:
        pivot = partition(nums, beg, end)
        quick_sort(nums, beg, pivot)
        quick_sort(nums, pivot + 1, end)


def partition(nums, beg, end):
    pivot_index = beg
    pivot = nums[pivot_index]
    left, right = pivot_index + 1, end - 1

    while True:

        while left <= right and nums[left] < pivot:
            left += 1

        while left <= right and nums[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            nums[left], nums[right] = nums[right], nums[left]

    nums[right], nums[pivot_index] = nums[pivot_index], nums[right]

    return right


if __name__ == '__main__':
    nums = [3, 4, 7, 2, 2, 18, 12]
    quick_sort(nums, 0, len(nums))
    print("result is", nums)
