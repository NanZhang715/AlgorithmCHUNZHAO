**学习总结**

**简单题目**
- [x 的平方根（字节跳动、微软、亚马逊在半年内面试中考过）](mySqrt.py)
- [有效的完全平方数（亚马逊在半年内面试中考过）](isPerfectSquare.py)
- [多数元素 （亚马逊、字节跳动、Facebook 在半年内面试中考过）](majorityElement.py)
- [柠檬水找零（亚马逊在半年内面试中考过）](lemonadeChange.py)
- [买卖股票的最佳时机 II （亚马逊、字节跳动、微软在半年内面试中考过）](maxProfit.py)
- [分发饼干（亚马逊在半年内面试中考过）](findContentChildren.py)
- [模拟行走机器人](robotSim.py)
 
**中等题目**
- [Pow(x, n) （Facebook 在半年内面试常考）](myPow.py)
- [子集（Facebook、字节跳动、亚马逊在半年内面试中考过）](subsets.py)
- [电话号码的字母组合（亚马逊在半年内面试常考）](letterCombinations.py)
- 单词接龙（亚马逊在半年内面试常考）
- 岛屿数量（近半年内，亚马逊在面试中考查此题达到 350 次）
- 扫雷游戏（亚马逊、Facebook 在半年内面试中考过）
- [跳跃游戏 （亚马逊、华为、Facebook 在半年内面试中考过）](canJump.py)
- [搜索旋转排序数组（Facebook、字节跳动、亚马逊在半年内面试常考）](search.py)
- [搜索二维矩阵（亚马逊、微软、Facebook 在半年内面试中考过）](searchMatrix.py)
- [寻找旋转排序数组中的最小值（亚马逊、微软、字节跳动在半年内面试中考过）](findMin.py)

**困难题目**
- N 皇后（字节跳动、苹果、谷歌在半年内面试中考过）
- 单词接龙 II （微软、亚马逊、Facebook 在半年内面试中考过） 
- [跳跃游戏 II （亚马逊、华为、字节跳动在半年内面试中考过）](jump.py)

**学习总结**

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
    - 494 目标和
    - 518 零钱兑换 II（组合问题， 与组合总和 IV，递推公式一样，遍历顺序完全不同） 
    - 322 零钱兑换 （组合最少问题）
    
```
1 二分查找问题总结

    单调性/上下边界/索引访问

2. 贪心和动态规划

    共同点：
    
    问题能够分解成子问题来解决，子问题的最优解能够递推到最终问题的最优解。
    这种子问题最优解称为最优子结构
    
    区别：
    
    对于最优子结构，贪心不能回退， 动态规划则保留以前的运算结果，并根据当前状态做出选择
            

3 Python 负数取余

   计算公式 
    - step 1: c = a/b 
    - step 2: r = a - c*b
  
  示例： 
    - 12%5 = 2,  
    - 12//5 = 2, 
    - 2 = 12 - 2*5
  对于模运算 和 取余 在第一步不同， 取余 向 0 的方向舍入，取模向 -"inf" 方向舍入
  
  结论：
    - 符号相同是， mod() 与 % 结果相同
    - 符号不同时，求模运算结果的符号 和 b一致，求余运算结果的符号和a一致
    - 在C/C++, C#, JAVA, PHP这几门主流语言中，%运算符都是做取余运算，而在python中的%是做取模运算
```