#https://leetcode.cn/problems/longest-common-subsequence/
'''
解题思路：
本题的要求在于不要求连续但还要保持相对顺序。

1.确定dp数组以及下标的含义

$$dp[i][j]：长度为[0,i-1]的字符串text1和长度为[0,j-1]的字符串的最长公共子序列为dp[i][j]$$

2.确定递推公式

$$主要存在如下两种情况，text1[i-1]与text2[j-1]相同，text1[i-1]与text2[j-1]不相同$$

$$如果text1[i-1]==text2[j-1]，则找到一个公共元素，所以dp[i][j]=dp[i-1][j-1]+1$$

$$如果text1[i-1]与text2[j-1]不相同，那就看看text1[0,i-2]与text2[0,j-1]的最长公共子序列和text1[0,i-1]与text2[0,j-2]的最长公共子序列，取最大的，也就是dp[i][j]=max(dp[i-1][j],dp[i][j-1])$$

3.dp数组初始化

统一初始化为0

4.确定遍历顺序

从前向后从上到下遍历

5.举例推导dp数组
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)==1 and len(text2)==1 and text1[0]!=text2[0]:#特殊情况
            return 0
        dp=[[0 for i in range(len(text2)+1)]for i in range(len(text1)+1)]#创建状态转移数组
        for i in range(1,len(text1)+1):#进行遍历
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:#根据递推公式进行计算
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[len(text1)][len(text2)]#返回结果
