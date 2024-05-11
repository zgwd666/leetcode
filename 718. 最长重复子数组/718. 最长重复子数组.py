#https://leetcode.cn/problems/maximum-length-of-repeated-subarray/
'''
解题思路：
1.确定dp数组以及下标的含义

$$dp[i][j]：$$以i-1为结尾的A和以下标j-1为结尾的B，最长重复子数组长度为$$dp[i][j]$$

2.确定递推公式

根据$$dp[i][j]$$的定义，$$dp[i][j]$$只能由$$dp[i-1][j-1]$$推导出来

$$即当A[i-1]和B[j-1]相等的时候,dp[i][j]=dp[i-1][j-1]+1$$

3.dp数组初始化

$$dp[i][0]=dp[0][j]=0$$

4.确定遍历顺序

外层for循环遍历A，内层for循环遍历B

5.举例推导dp数组
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)==1 and len(nums2)==1 and nums1[0]!=nums2[0]:#判断特殊情况
            return 0
        dp=[[0 for i in range(len(nums2)+1)] for i in range(len(nums1)+1)]#创建状态转移数组
        result=0#初始化结果
        for i in range(1,len(nums1)+1):#进行遍历
            for j in range(1,len(nums2)+1):
                if nums1[i-1]==nums2[j-1]:#根据递推公式进行计算
                    dp[i][j]=dp[i-1][j-1]+1
                if dp[i][j]>result:#重置最大值
                    result=dp[i][j]
        return result#返回结果
