#https://leetcode.cn/problems/squares-of-a-sorted-array/
'''
解题思路：采用双指针的方法
具体为：
因为数组为非递减数组，所以左边要么时最小的正数，要么是最小的负数，右边要么是最大的正数，要么是最大的负数，所以最大值肯定在左右两个元素中间
初始化左右指针分别指向数组的两端，不断对比二者平方大小，把最大的数从右往左填入结果数组，然后移动左右指针，直到遍历哇所有的数值。
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)#初始化结果数组
        left,right,k=0,len(nums)-1,len(nums)-1#初始化左右指针和k
        while left<=right:#进行遍历
            if nums[left]*nums[left]>nums[right]*nums[right]:#左边平方大，则将左边放入数组中
                res[k]=nums[left]*nums[left]
                k-=1#k-1
                left+=1#左边界右移
            else:
                res[k]=nums[right]*nums[right]#右边平方大，则将右边放入数组中
                k-=1
                right-=1#有边界左移
        return res
                
