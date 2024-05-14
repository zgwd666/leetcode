#https://leetcode.cn/problems/longest-palindromic-subsequence/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]:字符串s在[i,j]范围内的最长的回文子序列的长度为dp[i][j]$$

2.确定递推公式

如果s[i]与s[j]相同，则有$$dp[i][j]=dp[i+1][j-1]+2$$

如果s[i]与s[j]不相同，说明s[i]和s[j]同时加入并不能增加[i,j]区间回文子序列的长度，那么分别加入s[i]、s[j]看看哪一个可以组成中最长的回文子序列,则有$$dp[i][j]=max(dp[i+1][j],dp[i][j-1])$$

3.dp数组初始化

递推公式是计算不到i和j相同的情况。所以需要初始化$$dp[i][i]$$

4.确定遍历顺序

从下到上，从左到右遍历

5.举例推导dp数组

'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[0 for i in range(len(s))]for i in range(len(s))]#创建状态转移数组
        for i in range(len(s)):#进行初始化
            dp[i][i]=1
        for i in range(len(s)-1,-1,-1):#从下到上
            for j in range(i+1,len(s)):#从左到右
                if s[i]==s[j]:#相等时候的递推公式
                    dp[i][j]=dp[i+1][j-1]+2
                else:#不等时候的递推公式
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]#返回结果
