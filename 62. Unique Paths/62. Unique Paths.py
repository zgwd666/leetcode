#https://leetcode.cn/problems/unique-paths/
'''
解题思路：采用动态规划的思路，确定递推公式为dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，并初始化第一行第一列的值都为1
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths=[[0] * n for _ in range(m)]#创建状态转移数组
        for i in range(m):#将第一列的值都设置为1
            paths[i][0]=1
        for j in range(n):#将第一行的值都设置为1
            paths[0][j]=1
        for i in range(1,m):#进行遍历
            for j in range(1,n):
                paths[i][j]=paths[i-1][j]+paths[i][j-1]#计算递推公式
        return paths[m-1][n-1]#返回结果
