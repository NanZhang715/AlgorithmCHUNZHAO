 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
矩阵的乘法

1.  矩阵乘积 (dot product, matrix product, matmul product, inner product)：
    dot product (A, B): A 向量在B 向量上的投影
    
    a = [a1, a2, ..., an]
    b = [b1, b2, ..., bn]
    a . b = sum(a1b1 + a2b2 +... + anbn) 
    
    matmul 与 dot 有两点不同：
    - matmul 不支持标量
    -  Stacks of matrices are broadcast together as if the matrices were elements, 
        respecting the signature (n,k),(k,m)->(n,m)
     - 在处理高纬度时不同
    
    
2. Hadamard product(又称element-wise product)
    两矩阵对应元素相乘

3. Kronecker product(克罗内克积): 两个任意大小矩阵间的运算， A 的每个元素逐个与矩阵 B 相乘。

 行列互换得到转置矩阵
https://blog.finxter.com/numpy-matmul-operator/
"""

import numpy as np
# import tensorflow as tf
# import keras

# 2*3
a = [
    [1, 2, 2],
    [4, 5, 8]]

# 3*3
b = [
    [3],
    [1],
    [2]]


def dot_product(A, B):
    """
    合法检验：
        A 的列数 = B 的行数
    最终结果:
        A 的行数 * B 的列数, 即 (n, k), (k,m) ->(n,m)
    计算公式： a dot b = a * transpose(b)
    Returns:  返回矩阵为 A 行数 * B 列数
    https://blog.finxter.com/numpy-matmul-operator/
    """
    row_a, col_a = len(A), len(A[0])
    row_b, col_b = len(B), len(B[0])

    # A 的列数 必须等于 B 的行数
    if col_a != row_b:
        return -1

    rst = [[0]*col_b for _ in range(row_a)]

    # 先计算 b 的转置
    transpose_b = transpose(b)

    # 对应位置相乘
    for i in range(row_a):
        for j in range(col_b):
            rst[i][j] = sum([i*j for i, j in zip(A[i], transpose_b[j])])
    return rst


def transpose(matrix):
    """
    行列互换得到转置矩阵
    """

    m, n = len(matrix), len(matrix[0])
    rst = [[0]*m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            rst[j][i] = matrix[i][j]
    return rst


if __name__ == '__main__':
    # a . b = abT
    print("np dot product", np.dot(np.array(a), np.array(b)))
    print("np matmul", np.matmul(a, b))
    # print("transpose is", transpose(b))
    print("self define is", dot_product(a, b))