#https://leetcode.cn/problems/sqrtx/description/
'''
解题思路：采用二分法的思想，不断的逼近，需要注意的是，因为要舍去小数部分，所以最后的结果是向下取整，即i-1
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        i,j=0,x#初始化区间
        while i<=j:
            m=i+(j-i)//2#计算中点
            nums=m**2#计算中点的平方值
            if nums<x:#小则i变为m-1
                i=m+1
            elif nums>x:#大则j变为m-1
                j=m-1
            else:#相等则返回m
                return m
        return i-1#返回向下取整的结果
