#https://leetcode.cn/problems/perfect-squares/
'''
解题思路：
1.确定dp数组以及下标的含义

dp[j]:和为j的完全平方数的最少数量为dp[j]

2.确定递推公式

dp[j]=min(dp[j-i*i]+1,dp[j])

3.dp数组初始化

dp[0]=0

非0下标的dp[j]初始值为最大值

4.遍历顺序

外层for遍历物品，内层for循环遍历背。

5.举例推导dp数组

**代码**
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf')]*(n+1)#初始化dp数组
        dp[0]=0#初始化下标0的值
        for i in range(1,int(n**0.5)+1):#遍历物品，这里面的物品就相等于1到根号n+1的所有数字
            for j in range(i*i,n+1):#遍历背包
                dp[j]=min(dp[j-i*i]+1,dp[j])#进行递推公式计算
        return dp[-1]#返回结果
