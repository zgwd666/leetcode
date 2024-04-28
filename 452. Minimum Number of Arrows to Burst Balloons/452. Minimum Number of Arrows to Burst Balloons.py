#https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
'''
解题思路：计算重叠区域，尽可能多的重叠以减少弓箭数量。
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==1:#当仅有一个气球，那么只需要一个弓箭
            return 1
        points.sort(key=lambda x:(x[0]))#对气球进行排序，按照左边界进行升序排序
        count=1#初始化计数，因为第一个需要一个弓箭
        for i in range(1,len(points)):#进行遍历
            if points[i][0]>points[i-1][1]:#如果当前的左边界超过之前的有边界（没有等于是因为等于也算重叠）
                count+=1#需要额外的弓箭
            else:
                points[i][1]=min(points[i][1],points[i-1][1])#更新重叠的最小右边界
        return count#返回计数
