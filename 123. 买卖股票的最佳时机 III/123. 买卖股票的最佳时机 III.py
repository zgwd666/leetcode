#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
'''
解题思路：
本题的关键在于至多买卖两次，这意味着可以买卖一次，可以买卖两次，也可以不买卖

1.dp数组以及下标的含义

一天一共存在五个状态

0.没有操作

1.第一次持有股票

2.第一次不持有股票

3.第二次持有股票

4.第二次不持有股票

$$dp[i][j]$$：i代表为第i天，j代表[0-4]五个状态。$$dp[i][j]$$表示第i天状态j所剩的最大现金

2.确定递推公式

达到$$dp[i][1]$$状态，有两个具体操作：

- 第i天买入股票，则$$dp[i][1]=dp[i-1][0]-prices[i]$$
- 第i天没有操作，则$$dp[i][1]=dp[i-1][1]$$

所以$$dp[i][1]=max(dp[i-1][0]-prices[i],dp[i-1][1])$$

同理$$dp[i][2]$$也有两个操作：

- 第i天卖出股票，则$$dp[i][2]=dp[i-1][1]+prices[i]$$
- 第i天没有操作，则$$dp[i][2]=dp[i-1][2]$$

$$dp[i][2]=max(dp[i-1][1]+prices[i],d[i-1][2])$$

同理可得

$$dp[i][3]=max(dp[i-1][2]-prices[i],dp[i-1][3])$$

$$dp[i][4]=max(dp[i-1][3]+prices[i],d[i-1][4])$$

3.dp数组的初始化

第0天没有操作，$$dp[0][0]=0$$

第0天做第一次买入的操作，$$dp[0][1]=-prices[0]$$

第一天做卖出的操作，也就是当天买当天卖,$$dp[0][2]=0$$

同理

$$dp[0][3]=-prices[0]$$

$$dp[0][4]=0$$

4.确定遍历顺序

从前向后遍历

5.举例推导dp数组
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        dp=[[0 for _ in range(5)]for _ in range(len(prices))]#初始化状态啊转移数组
        dp[0][1]=dp[0][3]=-prices[0]#初始化第0天的状态
        for i in range(1,len(prices)):#进行遍历
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])#第一种状态
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])#第二种状态
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])#第三种状态
            dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])#第四种状态
        return max(dp[-1])#返回结果
