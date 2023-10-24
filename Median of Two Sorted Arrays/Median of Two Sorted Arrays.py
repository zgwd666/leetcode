#https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
'''
解题思路：
将两个数组合并，然后采用升序排序的方式将新的数组进行排序，之后进行中位数的计算
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #进行数组合并
        for i in nums2:
            nums1.append(i)
        #遍历新生成的数组，进行升序排序
        for i in range(len(nums1)):
            for j in range(i,len(nums1)):
                if nums1[i]>nums1[j]:
                    nums1[i],nums1[j]=nums1[j],nums1[i]
        #对排序好的数据进行中位数的计算，如果是单数的数组，取中间的数即可，如果是双数的数组，取中间两个数的平均数
        length=len(nums1)
        if length%2==1:
            avg=nums1[length//2]
        else:
            avg=(nums1[length//2-1]+nums1[length//2])/2
        return avg
