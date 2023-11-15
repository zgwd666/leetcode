#https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
'''
解题思路：
因为要原地更新数组，所以采用双指针的方式
定义左右两个指针，初始化值为0，1
不断遍历，直到右指针超出边界
在遍历的过程中，如果左指针的数字和右指针不同，则将左指针前移，并更新值为右指针的值；
如果相同，则右指针继续后移，以找到不重复的元素。
最终返回左指针+1就是长度
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return 1#如果仅有一个元素，那么就不存在重复项
        l,r=0,1#初始化左右指针
        while r<len(nums):#进行遍历
            if nums[l]!=nums[r]:果左指针的数字和右指针不同，则将左指针前移，并更新值为右指针的值；
                l+=1
                nums[l]=nums[r]
            else:如果相同，则右指针继续后移，以找到不重复的元素。
                r+=1
        return l+1#返回左指针+1就是长度
