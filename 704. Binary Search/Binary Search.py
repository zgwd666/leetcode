#https://leetcode.cn/problems/binary-search/description/
'''
解题思路：
采用二分法的思想，使用左闭右闭的区间。
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0#初始化左边界
        right=n-1#初始化右边界
        while left<=right: #因为是左闭右闭区间，所以[left,left]区间合法，所以是小于等于
            mid=(right-left)//2+left#取中间值，防止数值溢出
            #进行相关判断
            if nums[mid]==target:#找到，返回下标
                return mid
            if nums[mid]<target:#如果下标为middle的元素小于target，此时更新左边界。因为是左闭右闭区间，且判断结果显示，下标为middle的元素一定不是我们要搜索的值，所以我们更新左边界为middel+1
                left=mid+1
            if nums[mid]>target:#如果下标为middle的元素大于target，此时更新右边界。因为是左闭右闭区间，且判断结果显示，下标为middle的元素一定不是我们要搜索的值，所以我们更新右边界为middel-1
                right=mid-1
        return -1
