#https://leetcode.cn/problems/longest-increasing-subsequence/
'''
解题思路：
1.dp数组以及下标的含义

dp[i]表示i之前包括i的以nums[i]结尾的最长递增子序列的长度

2.状态转移方程

位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。

所以$$if (num[i]>nump[j]):dp[i]=max(dp[i],dp[j]+1)$$

3.dp数组的初始化

dp[i]=1

4.确定遍历顺序

从前向后遍历得到i

从前向后遍历i得到j

5.举例推导dp数组
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==1:#判断特殊情况
            return 1
        dp=[1]*len(nums)#进行初始化
        result=1#初始化最长长度指示器
        for i in range(len(nums)):#遍历数组
            for j in range(i):
                if nums[i]>nums[j]:#状态转移方程
                    dp[i]=max(dp[i],dp[j]+1)
            result=max(result,dp[i])#最长长度的计算
        return result#返回结果
