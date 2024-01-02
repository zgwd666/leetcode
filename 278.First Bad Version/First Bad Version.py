#https://leetcode.cn/problems/first-bad-version/description/
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
'''
解题思路：首先可以确定的是存在一个错误的版本。采用二分法，找到调用接口为True的第一个索引
'''
class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j=0,n#定义闭区间
        while i<=j:
            m=i+(j-i)//2#定义中点
            if isBadVersion(m):#中点是错误的版本，继续往前找
                j=m-1
            else:#中点是正确的版本，往后找
                i=m+1
        return i#返回调用接口为True的第一个索引
        
