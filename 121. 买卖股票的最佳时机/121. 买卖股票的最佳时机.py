#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
'''
解题思路：本题的关键在于在最低的时间点买入，在最高点进行卖出。
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        dp=[0]*len(prices)
        minPrice=prices[0]
        for i in range(1,len(prices)):
            minPrice=min(minPrice,prices[i])#提取出最低的价格
            dp[i]+=max(dp[i-1],prices[i]-minPrice)#计算最高的收益
        return dp[-1]
