#https://leetcode.cn/problems/merge-intervals/
'''
解题思路：求出重叠区域，然后更新区间为两个区间的并集。
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:return intervals#判断特殊情况
        intervals.sort(key=lambda x:x[0])#按照区间的左边界进行升序排序
        result=[]#初始化结果
        for i in range(1,len(intervals)):#进行遍历
            if intervals[i][0]<=intervals[i-1][1]:#如果存在重叠，更新区间为两个区间的并集
                intervals[i][0]=min(intervals[i][0],intervals[i-1][0])
                intervals[i][1]=max(intervals[i][1],intervals[i-1][1])
            else:#区间不重叠，将前一个区间添加到结果中
                result.append(intervals[i-1])
        result.append(intervals[-1])#因为遍历的时候最后一个区间没有加进去，此时补加进去
        return result#返回结果
