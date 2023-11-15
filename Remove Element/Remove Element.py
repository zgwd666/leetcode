#https://leetcode.cn/problems/remove-element/description/
'''
解题思路：将num里面等于val的数用超过nums正常范围的数字代替，然后进行排序，遍历排序后的数组，遇到设定的数字跳出，记录长度
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        if n==0:return 0#数组为空，返回0
        for i in range(len(nums)):#遍历数组将val用超过范围的值替代
            if nums[i]==val:
                nums[i]=-1
        for i in range(len(nums)):#遍历数组进行排序，目的是将设定的值移到数组的最后面
            for j in range(i,len(nums)):
                if nums[i]<nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        count=0#初始化长度
        for i in range(len(nums)):#遍历数组记录长度，直到遇到设定的 值跳出遍历
            if nums[i]!=-1:
                count+=1
            else:
                break
        return count#返回长度
