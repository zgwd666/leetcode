#https://leetcode.cn/problems/ransom-note/
'''
解题思路：采用空间换时间的策略，因为只涉及小写字母，则用一个长度为26的数组进行记录magazine出现字母的次数。然后再用ransomNote去验证这个数组是否包含了ransomNote所需要的所有字母。
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        temp=[0]*26#初始化一个长度为26的数组
        for i in range(len(magazine)):#记录magazine出现字母的次数
            temp[ord(magazine[i])-ord('a')]+=1
        for i in range(len(ransomNote)):#用ransomNote去验证这个数组是否包含了ransomNote所需要的所有字母
            temp[ord(ransomNote[i])-ord('a')]-=1
        for i in range(len(temp)):#对数组进行遍历，如果存在负数，也就是小于magazine的要求，就返回False
            if temp[i]<0:
                return False
        return True
