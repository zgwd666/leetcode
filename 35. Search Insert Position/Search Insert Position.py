#https://leetcode.cn/problems/search-insert-position/
'''
思路解析：本题就是一个二分查找的思想。分为以下两种情况
1.数组中存在target，则返回target对应的索引
2.不存在target，返回比target小的数中最靠右的索引
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1#先定义区间
        while i<=j:
            m=i+(j-i)//2#计算中点
            if target>nums[m]:
                i=m+1#target大，则i调整为m+1
            elif target<nums[m]:
                j=m-1#target小，则j调整为m-1
            else:
                return m#target找到，则返回target数对应的索引
        return i#数组不存在target数，返回比target小的数中最靠右的索引
