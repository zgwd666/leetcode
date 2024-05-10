#https://leetcode.cn/problems/longest-continuous-increasing-subsequence/
'''
解题思路：
1.dp数组以及下标的含义

dp[i]表示i之前包括i的以nums[i]结尾的最长递增子序列的长度

2.状态转移方程

因为要求连续，所以如果 nums[i] > nums[i - 1]，那么以 i 为结尾的连续递增的子序列长度 一定等于 以i - 1为结尾的连续递增的子序列长度 + 1 

所以$$if (num[i]>nump[j]):dp[idp[j]+1$$

3.dp数组的初始化

dp[i]=1

4.确定遍历顺序

从前向后遍历得到

5.举例推导dp数组
'''
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:#判断特殊情况
            return 1
        dp=[1]*len(nums)#初始化
        result=1#初始化最长长度指示器
        for i in range(1,len(nums)):#遍历数组
            if nums[i]>nums[i-1]:#状态转移方程
                dp[i]=dp[i-1]+1
            result=max(dp[i],result)#最长长度的计算
        return result#返回结果
