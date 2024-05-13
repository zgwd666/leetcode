#https://leetcode.cn/problems/distinct-subsequences/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]$$

2.确定递推公式

分为两种情况

$$s[i-1]==t[j-1]时dp[i][j]=dp[i-1][j-1]+dp[i-1][j]$$

$$当s[i-1]!=t[j-1]时dp[i][j]=dp[i-1][j]$$

3.dp数组初始化

$$dp[i][0]代表以i-1为结尾的字符串出现空字符串的个数，也就是1$$

$$dp[0][j]代表空字符串中出现以j-1为结尾的字符串t的个数，也就是0$$

$$dp[0][0]=1$$

4.确定遍历顺序

从上到下从左到右

5.举例推导dp数组

'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[0 for i in range(len(t)+1)]for i in range(len(s)+1)]#初始化状态转移数组
        for i in range(len(dp)):#进行初始化
            dp[i][0]=1
        for i in range(1,len(s)+1):#进行遍历
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:#当相等时，此时的个数等于考虑s当前的字符+不考虑s当前的字符
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:#不相等，只能不考虑s当前的字符
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]%(10**9+7)#返回结果
