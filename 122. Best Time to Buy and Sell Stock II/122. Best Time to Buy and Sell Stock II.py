#https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
'''
解题思路：最终的利润是可以拆解的，只需要计算出每天的价格减去前一天的价格作为前日购入本日抛售的利润，然后将所有的正利润相加即可
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:return 0#当数组中少于两个元素，返回0
        result=0#初始化利润
        for i in range(1,len(prices)):#进行遍历
            current=prices[i]-prices[i-1]#计算前日购入本日抛售的利润
            if current>0:#如果确实存在利润
                result+=current#将利润加到结果中
        return result#返回结果
