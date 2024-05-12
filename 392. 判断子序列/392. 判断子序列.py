#https://leetcode.cn/problems/is-subsequence/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]表示以i-1位结尾的字符串s,和以下标j-1为结尾字符串t，相同子序列的长度为dp[i][j]$$

2.确定递推公式

$$if s[i-1]==t[j-1] t中找到一个字符也在s中出现了 dp[i][j]=dp[i-1][j-1]+1$$

$$if s[i-1]!=t[j-1] 相当于t要删除元素，继续匹配 dp[i][j]=dp[i][j-1]$$

3.dp数组初始化

全部先初始化为0

4.确定遍历顺序

先外层遍历s，再内层遍历t

5.举例推导sp数组
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:#判断特殊情况
            return True
        if not t or len(s)>len(t):
            return False
        dp=[[0 for i in range(len(t)+1)]for i in range(len(s)+1)]#初始化状态转移数组
        for i in range(1,len(s)+1):#进行遍历
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:#找到一致元素
                    dp[i][j]=dp[i-1][j-1]+1
                else:#此时元素不一致
                    dp[i][j]=dp[i][j-1]
        if dp[-1][-1]==len(s):#判断s是否在t中出现
            return True
        return False
