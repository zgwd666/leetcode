#https://leetcode.cn/problems/non-overlapping-intervals/
'''
解题思路：基于左边界进行排序，发现重合的区间，则使得需要移除区间的数量+1，并且让当前的区间右边界变为重叠区间的最小值。
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:return 0#只有一个区间不需要移除
        count=0#移除区间的数量
        intervals.sort(key=lambda x:x[0])#按左边界排序
        for i in range(1,len(intervals)):#进行遍历
            if intervals[i][0]<intervals[i-1][1]:#发现重合的区间，则使得需要移除区间的数量+1，并且让当前的区间右边界变为重叠区间的最小值。
                count+=1
                intervals[i][1]=min(intervals[i][1],intervals[i-1][1])
        return count
