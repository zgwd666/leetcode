#https://leetcode.cn/problems/ones-and-zeroes/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]$$：最多有i个0和j个1的strs的最大子集的大小为$$dp[i][j]$$

2.确定递推公式

$$dp[i][j]$$可以由前一个strs的字符串推导出来，strs的字符串中由zeroNum个0,oneNun个1

$$dp[i][j]=max(dp[i][j],dp[i-zeroNum]dp[j-oneNun]+1)$$

3.dp数组的初始化

全部初始化为0，保证递推的时候$$dp[i][j]$$不会被初始值覆盖

4.确定遍历顺序

外层for循环遍历物品，内层for循环遍历背包容量且从后向前遍历

5.举例推导dp数组
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0] * (n + 1) for _ in range(m + 1)]#创建状态转移数组
        for s in strs:#对每一个数字进行遍历
            zeroNum=s.count('0')#统计0的个数
            oneNuns=s.count('1')#统计1的个数
            for i in range(m,zeroNum-1,-1):
                for j in range(n,oneNuns-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zeroNum][j-oneNuns]+1)#进行递推
        return dp[m][n]
