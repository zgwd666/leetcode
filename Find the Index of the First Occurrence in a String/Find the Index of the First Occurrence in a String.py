#https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
'''
解题思路：利用两个指针固定长度去寻找一致的字符串
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)==1 and len(needle)==1 :#当二者长度都为1，则直接对比，相等返回0，不等返回-1
            if haystack!=needle:
                return -1
            else:
                return 0
        if len(haystack)<len(needle):#如果待查找字符串比字串更小，直接返回-1
            return -1
        l,r=0,len(needle)#固定左右指针宽度
        while r<=len(haystack):#进行遍历
            if haystack[l:r]==needle:#第一次遇到相等，就直接返回左边下标
                return l
            else:#否则一起向前移动
                l+=1
                r+=1
        return -1#遍历完成仍然没找到，那就返回-1
