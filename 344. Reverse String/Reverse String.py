#https://leetcode.cn/problems/reverse-string/
'''
解题思路：
可以直接切片反转s[:]=s[::-1](s=s[::-1]是不改变元素组，创建改变的副本)
也可以使用双指针的方式，定义左右两个指针，同时向中间移动，并交换值
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1#定义左右两个指针
        while l<r:#开始遍历，知道左指针跑到右指针的右边
            s[l],s[r]=s[r],s[l]#交换左右指针代表的元素
            l+=1#左指针右移
            r-=1#右指针左移
