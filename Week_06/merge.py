#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

链接：https://leetcode-cn.com/problems/merge-intervals
"""
from typing import List
import heapq


class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, others):

        return self.start < others.start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        """
        时间复杂度 O(nlogn), 堆排 nlogn， 最终线性合并 n， O(n + nlogn)
        空间复杂度 O(n)
        """

        heap = []
        for s in intervals:
            if s:
                line = Line(s[0], s[1])
                heapq.heappush(heap, line)

        rst, prev = [], heapq.heappop(heap)

        while heap:
            cur = heapq.heappop(heap)

            # 如果相交，进行合并， 否则 prev 加入结果， 更新 prev
            if prev.end >= cur.start:
                prev = Line(prev.start, max(prev.end, cur.end))
            else:
                rst.append([prev.start, prev.end])
                prev = cur

        # 最后一个区间,
        # 1) if 和前一个相交，最终统一合并成 prev
        # 2）if 不相交，prev 加入到最终结果中
        if prev:
            rst.append([prev.start, prev.end])

        return rst


if __name__ == '__main__':

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [2, 3]]
    rst = Solution().merge(intervals)
    print("result is", rst)

