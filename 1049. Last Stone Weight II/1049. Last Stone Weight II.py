#https://leetcode.cn/problems/last-stone-weight-ii/
'''
解题思路：尽量让石头分成重量相同的两堆，相撞之后剩下的石头最少，这样就转换为01背包问题
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp=[0]*15001#初始化数组
        sumHalf=sum(stones)//2#计算target
        for stone in stones:
            for j in range(sumHalf,stone-1,-1):
                dp[j]=max(dp[j],dp[j-stone]+stone)#求出target
        return sum(stones)-2*dp[sumHalf]#计算结果
