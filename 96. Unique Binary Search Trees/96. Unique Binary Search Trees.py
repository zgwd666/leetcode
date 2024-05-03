#https://leetcode.cn/problems/unique-binary-search-trees/
'''
解题思路：根据递推公式dp[i]+=dp[j-1]*dp[i-j];j-1是j为头节点左子树的数量，i-j是以j为头节点右子树节点数量进行动态规划
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n<3:return n#当n为1和2的时候，搜索树的数量分别为1和2
        dp=[0]*(n+1)#初始化状态转移数组
        dp[0]=1#初始化dp[0]
        for i in range(1,n+1):#遍历节点数量
            for j in range(1,i+1):#将确定节点数量内的每一个数字作为头节点参与计算
                dp[i]+=dp[j-1]*dp[i-j]#根据递推公式计算dp[i]
        return dp[n]#返回结果
