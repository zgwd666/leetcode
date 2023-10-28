#https://leetcode.cn/problems/3sum-closest/description/
'''
解题思路：
采用双指针的思路。

'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<=3:
            return sum(nums)
        res=0
        min_dist=1e6
        nums=sorted(nums)
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                cur_dist=s-target
                if cur_dist==0:
                    return s
                elif cur_dist<0 :
                    l+=1
                    if abs(cur_dist)<min_dist:
                        min_dist=abs(cur_dist)
                        res=s
                else:
                    r-=1
                    if cur_dist<min_dist:
                        min_dist=cur_dist
                        res=s
        return res
                    
