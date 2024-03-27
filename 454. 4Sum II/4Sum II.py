#https://leetcode.cn/problems/4sum-ii/
'''
解题思路：将原本的四层循环转换为两次两层循环
利用字典存放前两个数组元素和及其出现次数，然后通过计算后两个数组元素和和0之间的差异在字典中的值，让count加上即可
'''
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1={}#首先定义一个字典，key存放a+b,value存放a+b和出现的次数
        count=0#定义一个统计变量count，用来统计四个元素相加等于0出现的次数
        for i in range(len(nums1)):#遍历前两个数组，统计两个数组元素之和和出现的次数，存放在数组中
            for j in range(len(nums2)):
                sum1=nums1[i]+nums2[j]
                if sum1 not in dict1:
                    dict1[sum1]=1
                else:
                    dict1[sum1]+=1
        for i in range(len(nums3)):#遍历后两个数组，统计0-(c+d)在字典中出现的次数，使用count加上字典中key对应的value的次数
            for j in range(len(nums4)):
                sum1=nums3[i]+nums4[j]
                diff=0-sum1
                if diff in dict1:
                    count+=dict1[diff]
        return count#返回统计值count
