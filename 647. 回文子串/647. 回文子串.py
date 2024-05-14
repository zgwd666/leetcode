#https://leetcode.cn/problems/palindromic-substrings/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]:表示区间[i,j]的子串是否为回文子串，如果是，则dp[i][j]=True,不是则dp[i][j]=False$$

2.确定递推公式

整体上分为两种情况，分别为s[i]==s[j] 和s[i]!=s[j]

当s[i]!=s[j]，$$dp[i][j]=False$$

当s[i]==s[j]，又存在如下三种情况

​	1.当下标i和j相同，即为一个字符，当然是回文子串

​	2.当i和j相差为1，也是回文子串

​	3.当下标i和j相差大于1，此时需要根据$$dp[i+1]dp[j-1]$$来判断$$dp[i][j]$$

3.dp数组初始化

全部初始化为False

4.确定遍历顺序

从下到上从左到右遍历

5.举例推导dp数组
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[False for i in range(len(s))]for i in range(len(s))]#创建状态转移数组并初始化
        result=0#初始化结果
        for i in range(len(s)-1,-1,-1):#从下到上
            for j in range(i,len(s)):#从左到右遍历
                if s[i]==s[j] and(j-i<=1 or dp[i+1][j-1]):#满足条件，进行递推
                    result+=1
                    dp[i][j]=True
        return result#返回结果
