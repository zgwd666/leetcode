#https://leetcode.cn/problems/combination-sum-iv/
'''
解题思路：
本题是求排列，完全一致的元素顺序不一致算两个不同的组合。

1.确定dp数组以及下标的含义

dp[i]:凑成目标正整数为i的排列个数为dp[i]

2.确定递推公式

dp[j]=dp[j-num[i]]

3.dp数组初始化

dp[0]=1

4.确定遍历顺序

排列问题先遍历背包后遍历物品

5.举例推导dp数组
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0]*(target+1)#初始化状体转移数组
        dp[0]=1#初始化
        for i in range(1,target+1):#排列问题先遍历背包
            for num in nums:#再遍历物品
                if i>=num:#当背包空间足够时
                    dp[i]+=dp[i-num]#进行计算
        return dp[-1]
