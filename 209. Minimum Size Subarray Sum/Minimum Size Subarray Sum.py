#https://leetcode.cn/problems/minimum-size-subarray-sum/
'''
解题思路：滑动窗口
定义双指针，一个慢指针用于指示连续子数组终止位置，快指针用于指示连续子数组终止位置。不断移动快指针，知道子数组和大于等于target，此时不断右移左指针以获得最小数组长度。
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen=len(nums)+1#先给最小长度初始化一个最大的值
        sum=0#定义前缀和
        slow=0#定义慢指针
        for i in range(len(nums)):#遍历快指针
            sum+=nums[i]#计算前缀和
            while sum>=target:#如果前缀和大于等于target，获取长度并于最小长度进行对比赋值操作，再弹出左侧数组元素，慢指针右移，重复上述过程直至sum<target
                current=i-slow+1
                if current<minLen:
                    minLen=current
                sum-=nums[slow]
                slow+=1
        if minLen<len(nums)+1:return minLen#判断最小长度是否存在，存在则返回，否则返回0
        return 0
