#https://leetcode.cn/problems/partition-equal-subset-sum/
'''
解题思路：采用0-1背包的思路。
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums)<2:return False#判断特殊情况
        dp=[0]*10001#初始化一维数组
        sumTotal=sum(nums)#计算数组总和
        if sumTotal%2==1:#当数组的和为奇数时，无法分割为两个整数，返回False
            return False
        sumHalf=sumTotal//2#计算target，也就是一半的sum
        for num in nums:
            for j in range(sumHalf,num-1,-1): # 每一个元素一定是不可重复放入，所以从大到小遍历
                dp[j]=max(dp[j],dp[j-num]+num)
        if dp[sumHalf]==sumHalf:# 集合中的元素正好可以凑成总和target
            return True
        return False
