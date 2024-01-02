#https://leetcode.cn/problems/missing-number/description/
'''
解题思路；先排序，再遍历
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()#排序
        for i in range(n+1):#遍历
            if i not in nums:
                return i
