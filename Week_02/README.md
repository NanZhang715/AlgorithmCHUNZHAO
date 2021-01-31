### 学习笔记

**简单题目**

- [N 叉树的后序遍历（亚马逊在半年内面试中考过）](n_tree_postorder.py)
- [N 叉树的前序遍历（亚马逊在半年内面试中考过）](preorderTraversal.py)
- [最小的 k 个数（字节跳动在半年内面试中考过）](getLeastNumbers.py)
- [二叉树的最大深度（亚马逊、微软、字节跳动在半年内面试中考过）](maxDepth.py) 
- [二叉树的最小深度（Facebook、字节跳动、谷歌在半年内面试中考过）](minDepth.py)
- [翻转二叉树 (谷歌、字节跳动、Facebook 在半年内面试中考过)](invertTree.py)

**中等题目**
- [括号生成 (字节跳动在半年内面试中考过)](generateParenthesis.py)
- [验证二叉搜索树（亚马逊、微软、Facebook 在半年内面试中考过）](isValidBST.py)
- 二叉树的序列化与反序列化（Facebook、亚马逊在半年内面试常考）
- [二叉树的中序遍历（亚马逊、微软、字节跳动在半年内面试中考过）](inorder.py)
- [二叉树的前序遍历（谷歌、微软、字节跳动在半年内面试中考过）](preorderTraversal.py)
- 滑动窗口最大值（亚马逊在半年内面试中常考）(maxSlidingWindow.py)
- N 叉树的层序遍历
- [丑数（字节跳动在半年内面试中考过）](UglyNumber.py)
- [前 K 个高频元素（亚马逊在半年内面试中常考）](topKFrequent.py)
- [二叉树的最近公共祖先（Facebook 在半年内面试常考）](lowestCommonAncestor.py)
- [从前序与中序遍历序列构造二叉树（字节跳动、亚马逊、微软在半年内面试中考过）](buildTree.py)
- [组合（微软、亚马逊、谷歌在半年内面试中考过）](combine.py)
- [全排列（字节跳动在半年内面试常考）](permute.py)
- [全排列 II （亚马逊、字节跳动、Facebook 在半年内面试中考过)](permuteUnique.py)
- [岛屿数量 dfs](numIslands.py)


**学习总结**

- [堆的实现 (主要总结操作逻辑以及时间复杂度)](min_heap.py)
- TopK： heap 和 部分快拍， 根据主定理 其中快排的时间复杂度 为O(n)
- dfs + 剪枝
  - 网格中搜索问题，例如岛屿问题，
    - [岛屿数量](numIslands.py)
    - [岛屿的周长](islandPerimeter.py)
    - [岛屿的最大面积](maxAreaOfIsland.py)，
    - 最大人工岛
  - 矩阵中路径问题的，例如 [矩阵中的路径](exist.py)
  - 二叉树路径问题,
    - [二叉树的所有路径](binaryTreePaths.py)
    - [求根到叶子节点数字之和](sumNumber.py)
    - [路径总和 II](pathSum.py)
- bfs 解决子集问题
  - [subsets 可以使用 bfs 或者 Lexicographic Subsets binmask 的方法进行解决](subset.py)
- 递归三要素
  - 终止条件
  - level task
  - level return
  
