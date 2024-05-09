#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/
'''
解题思路：
1.确定dp数组以及下标的含义

使用二维数组$$dp[i][j]$$：第i天的状态为j，所剩下的最大现金为$$dp[i][j]$$

j的状态表示为：

- 0表示不操作
- 1表示第一次买入
- 2表示第一次卖出
- 3表示第二次买入
- 4表示第二次卖出
- .....

除了0以外，偶数就是卖出，奇数就是买入

题目要求至多有k笔交易，那么j的范围定义为2*k+1

2.确定递推公式

当j为奇数时：

$$dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]-prices[i])$$

当j为偶数时：

$$dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+prices[i])$$

3.dp数组初始化

$$dp[0][j]=-prices[0] j为奇数 dp[0][j]=0 j为偶数$$

4.确定遍历顺序

从前向后遍历

5.举例推导dp数组
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)==1:#判断特殊情况
            return 0
        dp=[[0 for i in range(2*k+1)]for i in range(len(prices))]#初始化状态转移数组
        for i in range(2*k+1):#对第0天的奇数状态进行赋值
            if i%2==1:
                dp[0][i]=-prices[0]
        for i in range(1,len(prices)):#进行遍历
            for j in range(1,2*k+1):
                if j%2==0:#偶数状态的递推公式
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+prices[i])
                else:#奇数状态的递推公式
                     dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]-prices[i])
        return dp[-1][-1]#返回结果
