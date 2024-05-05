#https://leetcode.cn/problems/coin-change-ii/
'''
解题思路：
1.确定dp数组以及下标的含义

dp[j]：凑成总金额j的货币组合数为dp[j]

2.确定递推公式

dp[j]=dp[j-num[i]]

3.初始化dp数组

dp[0]=1

4.确定遍历顺序

先遍历物品后遍历背包

5.举例推导dp数组
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)#初始化状态转移数组
        dp[0]=1#初始化
        for coin in coins:#先遍历物品
            for i in range(coin,amount+1):#遍历背包
                dp[i]+=dp[i-coin]#计算递推公式
        return dp[-1]#返回结果
