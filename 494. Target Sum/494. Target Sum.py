#https://leetcode.cn/problems/target-sum/
'''
解题思路：假设加法的总和为x，则减法的总和就是sum-x
我们要求的是x-(sum-x)=target
也就是x=(target+sum)/2
也就是在背包问题中target=(target+sum)/2
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumTotal=sum(nums)#计算总和
        if sumTotal<target or (sumTotal+target)%2==1:#判断特殊情况
            return 0
        dp=[0]*10001#初始化数组
        dp[0]=1#初始化
        targetSum=(target+sumTotal)//2#计算目标和
        for num in nums:
            for j in range(targetSum,num-1,-1):
                dp[j]+=dp[j-num]
        return dp[targetSum]
