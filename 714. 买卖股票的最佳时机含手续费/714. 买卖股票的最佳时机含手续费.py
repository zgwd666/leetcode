#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]$$,第i天的状态为j，所剩的最多现金为$$dp[i][j]$$

具体可以区分出两种状态

1.不持有股票状态（今天卖出股票，或者之前就不持有股票状态）状态0

2.持有股票状态（今天买入股票，或者之前就只有股票状态）状态1

本次将手续费算到买入状态中

2.确定递推公式

$$ dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])$$

$$dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i]-fee)$$

3.dp数组初始化

$$dp[i][1]=-prices[0]-fee dp[i][0]=0$$

4.确定遍历顺序

从前向后遍历

5.举例推导dp数组
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)==1:#判断特殊情况
            return 0
        dp=[[0 for _ in range(2)]for i in range(len(prices))]#创建装填转移数组
        dp[0][1]=-prices[0]-fee#初始化
        for i in range(1,len(prices)):#进行遍历，按照两种情况的递推公式进行递推
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i]-fee)
        return max(dp[-1])#返回结果
