#https://leetcode.cn/problems/string-to-integer-atoi/description/
'''
解题思路：
先通过Python的内置函数去除左边的空格，然后将符号进行单独提取，之后将字符串内含数组通过映射列表一一提取，之后转换为数字加上正负号，与范围进行比较，最终输出结果
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        l1=['0','1','2','3','4','5','6','7','8','9']
        s2=''
        s=s.lstrip()
        flag=1
        if s=='':
            return 0
        else:
            if s[0]=='-':
                flag=-1
                s1=s[1:]
            elif s[0]=='+':
                flag=1
                s1=s[1:]
            else:
                s1=s

        for i in range(len(s1)):
            if s1[i] in l1:
                s2+=s1[i]
            else:
                break
        if s2=='':
            return 0
        s2=int(s2)*flag
        if s2>=(2**31)-1:
            return (2**31)-1
        elif s2<=-(2**31):
            return -(2**31)
        else:
            return s2
