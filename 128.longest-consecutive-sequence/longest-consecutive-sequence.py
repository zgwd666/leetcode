#https://leetcode.cn/problems/longest-consecutive-sequence/description/
'''
解题思路：现将数组排序，然后寻找数组中的最长连续子序列就行，判定标准为后一个等于前一个+1，注意重复数字的干扰
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0#数组中不存在数字，直接返回0
        nums=sorted(nums)#数组排序
        maxLength=1#初始化最大数字连续序列的长度
        cur_len=1#定义当前的数字连续序列的长度
        for i in range(1,len(nums)):#进行循环
            if nums[i]==nums[i-1]:continue#重复数字跳过
            if nums[i]==nums[i-1]+1:#判断是否连续，连续，当前的数字连续序列的长度+1
                cur_len+=1
            else:
                cur_len=1#不连续，当前的数字连续序列的长度重置为1
            if cur_len>maxLength:#更新初始化最大数字连续序列的长度
                maxLength=cur_len
        return maxLength
