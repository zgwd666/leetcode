#https://leetcode.cn/problems/min-cost-climbing-stairs/
'''
解题思路：采用动态规划的思路，确定了dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)#初始化状态转移数组，因为从最后一个元素跳上台阶也需要体力，所以需要+1
        for i in range(2,len(cost)+1):#从第三个元素开始遍历
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])#递推公式
        return dp[-1]#返回结果
