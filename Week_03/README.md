**学习总结**

**简单题目**

- [多数元素 （亚马逊、字节跳动、Facebook 在半年内面试中考过）](majorityElement.py)
- [柠檬水找零（亚马逊在半年内面试中考过）](lemonadeChange.py)
- 买卖股票的最佳时机 II （亚马逊、字节跳动、微软在半年内面试中考过）
- 分发饼干（亚马逊在半年内面试中考过）
- 模拟行走机器人
 
**中等题目**
- [Pow(x, n) （Facebook 在半年内面试常考）](myPow.py)
- [子集（Facebook、字节跳动、亚马逊在半年内面试中考过）](subsets.py)
- [电话号码的字母组合（亚马逊在半年内面试常考）](letterCombinations.py)
- 单词接龙（亚马逊在半年内面试常考）
- 岛屿数量（近半年内，亚马逊在面试中考查此题达到 350 次）
- 扫雷游戏（亚马逊、Facebook 在半年内面试中考过）
- 跳跃游戏 （亚马逊、华为、Facebook 在半年内面试中考过）
- 搜索旋转排序数组（Facebook、字节跳动、亚马逊在半年内面试常考）
- 搜索二维矩阵（亚马逊、微软、Facebook 在半年内面试中考过）
- 寻找旋转排序数组中的最小值（亚马逊、微软、字节跳动在半年内面试中考过）

**困难题目**
- N 皇后（字节跳动、苹果、谷歌在半年内面试中考过）
- 单词接龙 II （微软、亚马逊、Facebook 在半年内面试中考过） 
- 跳跃游戏 II （亚马逊、华为、字节跳动在半年内面试中考过）

**学习总结**

- 使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方。同学们可以将自己的思路、代码写在学习总结中。
- 组合问题
  - dfs 可解决
    - [子集(无重复) subset I](subsets.py) 
    - [子集(有重复) subset II](subsetsWithDup.py)    
    - [组合 Combinations](Week_02/combine.py)
    - [排列 I Permutations I](Week_02/permute.py)
    - [排列 II Permutations II](Week_02/permuteUnique.py)  
    - [组合总和 (可重复使用) combinationSum ](combinationSum.py)
    - [组合总和（不可重复使用）combinationSum II ](combinationSum2.py)
    - [组合总和 III combinationSum III](combinationSum3.py)
  - dp 可解决    
    - [377 组合总和 IV combinationSum IV (排列问题使用 dfs 超时, dp可解决，类似硬币找零)](combinationSum4.py)
    - 494. 目标和
    - 518. 零钱兑换 II（组合问题， 与组合总和 IV，递推公式一样，遍历顺序完全不同） 
    - 322. 零钱兑换 （组合最少问题）