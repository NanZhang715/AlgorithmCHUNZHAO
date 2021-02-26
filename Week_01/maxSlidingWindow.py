#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。
示例 1：

    输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
    输出：[3,3,5,5,6,7]

解释：
    滑动窗口的位置                最大值
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        思路：单调队列， 定义一个单调递减队列， 队列首个元素为最大，向后依次减小
            遍历nums，
                （1）元素 <= 最后一个元素，push 该元素的索引入队列
                （2）元素 > 最后一个元素, 否则 pop 队列右侧元素， 出栈直到 遇到更大的元素
        时间复杂度：O(n)
        空间复杂度：O(n)

        注意单调队列左右出的顺序
        """
        dequeue = deque([])

        for s in range(k):
            while dequeue and nums[s] > nums[dequeue[-1]]:  # 1) 判断 双端队列是否为空， 2) 是否单调递减
                dequeue.pop()  # pop 右侧出队列
            dequeue.append(s)

        rst = [nums[dequeue[0]]]
        for s in range(k, len(nums)):
            while dequeue and nums[s] > nums[dequeue[-1]]:
                dequeue.pop()  # pop 右侧出队列
            dequeue.append(s)

            # 判断最大值是否在窗口内
            while dequeue[0] <= s - k:
                dequeue.popleft()  # pop 左侧出队列

            rst.append(nums[dequeue[0]])
        return rst


if __name__ == '__main__':
    # nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    nums, k = [9, 10, 9, -7, -4, -8, 2, -6], 5
    rst = Solution().maxSlidingWindow(nums, k)
    print("result is", rst)
