#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

输入：matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]],
    target = 3
输出：true
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
        思路 题目中条件为每行单调递增，并没有说明每列也单调递增
         （1）合并 K 的链表的方法
            时间复杂度 O(nlogk)
            空间复杂度 O(logk)

         （2）变形的二分查找, 在二维矩阵搜索时，M*N 的矩阵中， M 为行数， N 为列数

            可利用条件有    row = mid//N, col = mid%N

            时间复杂度 O(logMN)
            空间复杂度 O(1)
            此题最适用于此方法

         ** 如果每列也是递增则可以使用以下两种方法

          (3) 剑指 offer 的方法， 沿着对角线，从右上角向开始查找，因为是有序数组，设 右上角元素 dp[i][j]
             - target > dp[i][j], 缩小行的范围 i -= 1
             - target > dp[i][j], 缩小列的范围 j -=1

            时间复杂度 O(logn)
            空间复杂度 O(1)

           (4) 二分法变形，需要一个辅助函数， 从左下角向右上角搜索， 辅助函数统计 比 target 大 的元素数量，
           也可用于 matrix topk 的搜索

            时间复杂度 O(logn)， 比第二种方法慢，因为这种方法 右边界不断二分，做边界不断尝试，一半二分，一半线性查找
            空间复杂度 O(1)
        """

        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = left + (right - left)//2
            pivot = matrix[mid//n][mid%n]
            if pivot == target:
                return True
            elif pivot > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 60]]
    target = 3
    rst = Solution().searchMatrix(matrix, target)
    print("result is", rst)


