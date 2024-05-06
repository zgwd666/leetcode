#https://leetcode.cn/problems/house-robber/
'''
解题思路：
当前房屋的状态取决于前一个房屋和前两个房屋是否被偷了。

1.确定dp数组以及下标的含义

dp[i]：考虑下标i以内的房屋，最多可以偷窃的金额为dp[i]

2.确定递推公式

决定dp[i]的因素就是第i个房间偷还是不偷

如果偷第i个房间，那么dp[i]=dp[i-2]+nums[i]，即：第i-1房一定是不考虑的，找出 下标i-2（包括i-2）以内的房屋，最多可以偷窃的金额为dp[i-2] 加上第i房间偷到的钱。

如果不偷第i房间，那么dp[i] = dp[i - 1]，即考 虑i-1房，（**注意这里是考虑，并不是一定要偷i-1房，**）

然后dp[i]取最大值，即dp[i] = max(dp[i - 2] + nums[i], dp[i - 1]);

3.dp数组初始化

dp数组的基础为dp[0]和dp[1]

dp[0]=nums[0]

dp[1]=max(nums[0],nums[1])

4.确定遍历顺序

从前向后遍历

5.举例推导dp数组
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:#判断特殊情况
            return nums[0]
        dp=[0]*len(nums)#初始化状态转移数组
        dp[0]=nums[0]#初始化dp[0]
        dp[1]=max(nums[0],nums[1])#初始化dp[1]
        for i in range(2,len(nums)):#从前向后遍历
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])#进行递推
        return dp[-1]#返回结果
