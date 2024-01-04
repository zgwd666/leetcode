#https://leetcode.cn/problems/move-zeroes/description/
'''
解题思路：采用冒牌排序的思想，将0交换到数组的最后
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==0 and nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
