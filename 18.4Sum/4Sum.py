#https://leetcode.cn/problems/4sum/description/
'''
解题思路：采用最原始的循环暴力解法
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:#当数组中不足四个数直接返回
            return []
        nums=sorted(nums)#将数组排序，从小到大
        res=[]#初始化结果列表
        for i in range(len(nums)):#三层循环
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    end_num=target-(nums[i]+nums[j]+nums[k])#检索结果以优化左右一层循环
                    if end_num in nums[k+1:] and [nums[i],nums[j],nums[k],end_num] not in res:#去重（因为已经排过序，可以采用该方法进行去重）
                        res.append([nums[i],nums[j],nums[k],end_num])#将结果添加到结果列表中
        return res
