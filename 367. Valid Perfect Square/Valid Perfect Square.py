#https://leetcode.cn/problems/valid-perfect-square/description/
'''
解题思路：因为正整数如果是完全平方数，则一定可以由小于等于其的正整数平方得到。也就是一定存在一个1-num区间的整数平方等于num，那就转换成求1-num之间的一个数的二分查找问题
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right=1,num#初始左右边界
        while left<=right:#进行循环
            mid=(right-left)//2+left#求区间中间
            if mid*mid==num:#如果mid的平方等于num，则返回true
                return True
            if mid*mid<num:#如果mid的平方小于num，则左边界等于mid+1
                left=mid+1
            if mid*mid>num:#如果mid的平方大于num，则右边界等于mid-1
                right=mid-1
        return False#没找到返回false
