#https://leetcode.cn/problems/word-break/
'''
解题思路：单词就是物品，字符串s就是背包，单词能否组成字符串s，就是问物品能不能把背包装满。

拆分的时候可以重复使用字典中的单词，说明就是一个完全背包！

1.确定dp数组以及下标的含义

dp[i]:字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词。

2.确定递推公式

如果确定dp[j]为true，且[j,i]这个区间的子串出现在字典中，那么dp[i]一定是true(j<i)

所以递推公式是if([j,i]这个区间的子串出现在字典里&&dp[j]是true)，那么dp[i]=true

3.dp数组如何初始化

dp[0]为true，其他下标的dp[j]为False

4.如何进行遍历

因为单词内的字符是存在顺序的，则本题求的就是排列

5.举例推导dp[i]
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 表示字符串的前 i 个字符是否可以被拆分成单词
        dp[0] = True  # 初始状态，空字符串可以被拆分成单词

        for i in range(1, n + 1): # 遍历背包
            for j in range(i): # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    break

        return dp[n]
