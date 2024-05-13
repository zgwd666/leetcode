#https://leetcode.cn/problems/delete-operation-for-two-strings/
'''
解题思路：
只需要求出两个字符串的最长公共子序列长度即可，那么除了最长的公共子序列之外的字符串都是必须删除的，最后用两个字符串的总长度监督两个最长公共子序列的长度就是删除的最少步数。
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0 for i in range(len(word2)+1)]for i in range(len(word1)+1)]#状态转移数组
        #计算最大子序列的长度
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return len(word1)+len(word2)-dp[-1][-1]*2#返回结果
