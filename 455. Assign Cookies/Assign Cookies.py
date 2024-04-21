#https://leetcode.cn/problems/assign-cookies/
'''
解题思路：采用贪心算法，以小孩数组为基础，不断移动饼干数组以进行判断
'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s:return 0#判断特殊情况
        count=0#初始化计数
        s.sort()#对饼干数组排序
        g.sort()#对小孩数组排序
        index=len(s)-1#初始化index
        for i in range(len(g)-1,-1,-1):#对小孩数组不断从后向前遍历
            if index>=0 and g[i]<=s[index]:#当饼干数组指向元素非空且满足条件
                index-=1#饼干数组指针向前移动
                count+=1#计数加一
        return count
