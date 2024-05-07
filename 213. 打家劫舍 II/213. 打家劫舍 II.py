#https://leetcode.cn/problems/house-robber-ii/
'''
解题思路：将问题拆解为三种情况：
1.考虑不包含首尾元素
2.考虑包含首元素，不包含尾元素
3.考虑包含尾元素，不包含首元素
2和3种涵盖了情况1
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:#判断特殊情况
            return nums[0]
        def rob(nums,start,end):#计算不是环形的最大金额
            if start==end-1:#如果数组中只存在一个元素
                return nums[start]
            dp=[0]*(len(nums)+1)#初始化状态转移数组
            #初始化数组的前两个值
            dp[start]=nums[start]
            dp[start+1]=max(nums[start],nums[start+1])
            #进行遍历，并根据递推公式进行计算
            for i in range(start+1,end):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[end-1]#返回结果
        resultHead=rob(nums,0,len(nums)-1)#第二种情况，去除尾部元素
        resultTail=rob(nums,1,len(nums))#第一种情况，去除头部元素
        result=max(resultHead,resultTail)#返回结果中的最大值
        return result
