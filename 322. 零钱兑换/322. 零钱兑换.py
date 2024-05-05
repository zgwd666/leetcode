#https://leetcode.cn/problems/coin-change/
'''
解题思路：
1.确定dp数组以及下标的含义

dp[j]:凑足总额为j所需钱币最少个数为dp[j]

2.确定递推公式

dp[j]=min(dp[j-coins[i]]+1,dp[j])

3.dp数组初始化

首先凑足总金额为0所需钱币的个数为0，dp[0]=0

其他的下标对应的数值必须先初始化一个最大的值

4.确定遍历顺序

**如果求组合数就是外层for循环遍历物品，内层for遍历背包**。

**如果求排列数就是外层for遍历背包，内层for循环遍历物品**。

本题可以采用先遍历物品后遍历背包

5.举例推导dp数组
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)#初始化值为最大
        dp[0]=0#初始化下标0
        for coin in coins:#先遍历物品
            for i in range(coin,amount+1):#再遍历背包
                if dp[i-coin]!=float('inf'): # 如果dp[i - coins[j]]不是初始值，则进行状态转移
                    dp[i]=min(dp[i],dp[i-coin]+1)# 更新最小硬币数量
        if dp[-1]==float('inf'): # 如果最终背包容量的最小硬币数量仍为正无穷大，表示无解
            return -1
        return dp[-1] # 返回背包容量为amount时的最小硬币数量
