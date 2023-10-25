#https://leetcode.cn/problems/integer-to-roman/description/
'''
解题思路：
先提取出千 百 十 个位上的数字，然后按照对照表进行一一对照，主要是注意400 900 40 90 4 9几个数字的表达即可
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        q=num//1000#提取千分位上的数字
        h=num//100-q*10#提取百分位上的数字
        s=num//10-100*q-10*h#提取十分位上的数字
        g=num%10#提取个位上的数字
        s1=''#创建空字符串用于存储结果
        s1+='M'*q#先将千分位上的数字转换
        if h==9:#转换900
            s1+='CM'
        elif h==4:#转换400
            s1+='CD'
        elif h<4:#转换小于400
            s1+='C'*h
        elif 9>h>=5:#转换500-900
            s1+='D'
            s1+='C'*(h-5)
        if s==9:#转换90
            s1+='XC'
        elif s==4:#转换40
            s1+='XL'
        elif s<4:#转换小于40
            s1+='X'*s
        elif 9>s>=5:#转换50-90
            s1+='L'
            s1+='X'*(s-5)
        if g==9:#转换9
            s1+='IX'
        elif g==4:#转换4
            s1+='IV'
        elif g<4:#转换小于4
            s1+='I'*g
        elif 9>g>=5:#转换5到9
            s1+='V'
            s1+='I'*(g-5)
        return s1
        
