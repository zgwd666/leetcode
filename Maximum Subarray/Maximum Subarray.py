#https://leetcode.cn/problems/maximum-subarray/description/
'''
解题思路：采用动态规划
设最优解dp[i]:
  如果dp[i-1]<=0,dp[i]=nums[i]
  如果dp[i-1]>0,dp[i]=dp[i-1]+nums[i]
初始状态dp[0]=num[0]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)#创建状态转移数组
        dp[0]=nums[0]#初始化状态
        for i in range(1,len(nums)):#进行遍历  如果dp[i-1]<=0,dp[i]=nums[i]  如果dp[i-1]>0,dp[i]=dp[i-1]+nums[i]
            if dp[i-1]>0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]
        return max(dp)#返回数组中最大值
