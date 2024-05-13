#https://leetcode.cn/problems/edit-distance/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]$$

2.确定递推公式

会出现四种情况

$$当word1[i-1]==word2[j-1]，此时不需要任何编辑，即dp[i][j]=dp[i-1][j-1]$$

$$当word1[i-1]!=word2[j-1],此时存在增删改三种操作$$

$$操作一：word1删除一个元素，那么就是以下标i-2为结尾的word1与j-1为结尾的word2的最近编辑距离再加上一个操作，即dp[i][j]=dp[i-1][j]+1$$

$$操作二：word2删除一个元素，那么就是以下标i-1为结尾的word1与j-2为结尾的word2的最近编辑距离再加上一个操作，即dp[i][j]=dp[i][j-1]+1$$

$$操作三：替换元素，将word1中word[i-1]的元素替换为word2[j-1]，此时不需要增删元素，即dp[i][j]=dp[i-1][j-1]+1$$

综合上述三种情况，可以得到$$当word1[i-1]!=word2[j-1],dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]+1)$$

3.dp数组初始化

$$dp[i][0]需要将word1中的字符串全部删完，也就是dp[i][0]=i$$

$$dp[0][j]需要将word1中的字符串全部删完，也就是dp[0][j]=j$$

4.确定遍历顺序

从左到右从上到下

5.举例推导dp数组
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0 for i in range(len(word2)+1)]for i in range(len(word1)+1)]#创建状态转移数组
        #进行初始化
        for i in range(len(dp)):
            dp[i][0]=i
        for j in range(len(dp[0])):
            dp[0][j]=j
        #进行递推
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:#相等时的递推公式
                    dp[i][j]=dp[i-1][j-1]
                else:#不等时的递推公式
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]#返回结果
