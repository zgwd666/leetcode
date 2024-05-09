#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''
解题思路：
在本题中，一共存在四种状态
不持有股票也不是冷却期状态 状态1
持有股票状态 状态2
卖出股票状态 状态3
冷静期状态
1.确定dp数组以及下标的含义
$$dp[i][j]$$,第i天的状态为j，所剩的最多现金为$$dp[i][j]$$
2.确定递推公式
 dp[i][0]=max(dp[i-1][0],dp[i-1][3])
 dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][3]-prices[i],dp[i-1][1])
 dp[i][2]=dp[i-1][1]+prices[i]
 dp[i][3]=dp[i-1][2]
 3.dp数组初始化
 dp[0][1]=-prices[0],dp[0][0]=dp[0][2]=dp[0][3]=0
4.确定遍历顺序

从前向后遍历

5.举例推导dp数组
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:#特殊状态
            return 0
        dp=[[0 for i in range(4)]for i in range(len(prices))]#初始化状态转移数组
        dp[0][1]=-prices[0]#初始化
        for i in range(1,len(prices)):#进行遍历，针对四个状态进行递推
            dp[i][0]=max(dp[i-1][0],dp[i-1][3])
            dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][3]-prices[i],dp[i-1][1])
            dp[i][2]=dp[i-1][1]+prices[i]
            dp[i][3]=dp[i-1][2]
        return max(dp[-1])#返回结果
