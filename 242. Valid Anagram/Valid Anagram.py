#https://leetcode.cn/problems/valid-anagram/
'''
解题思路：采用哈希表统计两个字符串中每个字符出现的次数，如果相等，返回true，否则返回false。
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False#长度不一致，肯定不是异位词
        s_cnt=[0]*26#初始化s哈希表
        t_cnt=[0]*26#初始化t哈希表
        for i in range(len(s)):#对每个元素进行遍历（因为保证了s和t长度一致）
            s_cnt[ord(s[i])-ord('a')]+=1#计算元素相对位置加一
            t_cnt[ord(t[i])-ord('a')]+=1#计算元素相对位置加一
        if s_cnt==t_cnt:#如果两个哈希表相等,返回true，
            return True
        else:#否则返回false
            return False
