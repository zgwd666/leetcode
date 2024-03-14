#https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
解题思路：分别使用两次二分查找，找到左右边界（不含）
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums,target):#寻找左边界
            left,right=0,len(nums)-1#初始化左右边界
            leftBoundary=-2#初始化左边界
            while left<=right:#进行循环
                mid=(right-left)//2+left#计算中间值
                if nums[mid]>=target:#当中间元素大于等于target，则执行右边界等于mid-1，并赋值给左边界的操作，这样计算出第一个小于target的元素的下标
                    right=
                    leftBoundary=right
                else:#否则，左边界等于mid+1 
                    left=mid+1 
            return leftBoundary#返回左边界
        def findRight(nums,target):#寻找右边界
            left,right=0,len(nums)-1#初始化左右边界
            rightBoundary=-2#初始化右边界
            while left<=right:#进行循环
                mid=(right-left)//2+left#计算中间值
                if nums[mid]<=target:#当中间元素小于等于target，则执行左边界等于mid+1 ，并赋值给左边界的操作，这样计算出第一个大于target的元素的下标
                    left=mid+1
                    rightBoundary=left
                else:#否则，右边界等于mid-1
                    right=mid-1 
            return rightBoundary#返回右边界
        leftBoundary=findLeft(nums,target)#获取左边界
        rightBoundary=findRight(nums,target)#获取右边界
        if leftBoundary==-2 or rightBoundary==-2:return[-1,-1]#对于第一种情况，即target处于区间的两侧
        if rightBoundary-leftBoundary>1:return[leftBoundary+1,rightBoundary-1]#因为求出的左右边界是分别小于和大于元素的第一个下标，所以如果右边界减去左边界小于等于1，则表示此元素不在数组中，最终的边界应该为[leftBoundary+1,rightBoundary-1],即第三种情况
        return [-1,-1]#对应第二种情况
