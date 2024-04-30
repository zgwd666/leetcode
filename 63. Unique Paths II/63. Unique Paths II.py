#https://leetcode.cn/problems/unique-paths-ii/
'''
解题思路：采用动态规划的思路，根据递推公式dp[i][j] = dp[i - 1][j] + dp[i][j - 1]结合障碍物的情况。
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)#获取行数
        n=len(obstacleGrid[0])#获取列数
        if obstacleGrid[m-1][n-1]==1:#如果最后一个位置有障碍物，就无法到达
            return 0
        dp=[[0]*n for i in range(m)]#创建状态转移数组
        for i in range(m):#对第一列进行赋值
            if obstacleGrid[i][0]==0:#当没有障碍物时，赋值为1
                dp[i][0]=1
            else:#存在障碍物的位置及其之后的位置都为0，因为只能一直向下才能到达位置
                break
        for j in range(n):#对第一行进行赋值
            if obstacleGrid[0][j]==0:#当没有障碍物时，赋值为1
                dp[0][j]=1
            else:#存在障碍物的位置及其之后的位置都为0，因为只能一直向右才能到达位置
                break
        for i in range(1,m):
            for j in range(1,n):#进行遍历
                if obstacleGrid[i][j]==0:#当位置不存在障碍物时才能进行路径计算
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]#返回最终的路径个数
