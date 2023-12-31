#https://leetcode.cn/problems/string-to-integer-atoi/description/
'''
解题思路：
先通过Python的内置函数去除左边的空格，然后将符号进行单独提取，之后将字符串内含数组通过映射列表一一提取，之后转换为数字加上正负号，与范围进行比较，最终输出结果
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        l1=['0','1','2','3','4','5','6','7','8','9']#建立数字映射列表，用于判断字符是否为数字
        s2=''#初始化空列表
        s=s.lstrip()#将字符串左侧的空格删除
        flag=1#定义正负号，默认是正，如果字符串在数字之前未出现正负号，则为正
        if s=='':#如果去除空格之后为空，即返回0
            return 0
        else:
            if s[0]=='-':#如果开始遇到了负号
                flag=-1#定义符号为负号
                s1=s[1:]#将符号去除，不影响接下来的判断
            elif s[0]=='+':#如果开始遇到了正号
                flag=1#定义符号为正号
                s1=s[1:]#将符号去除，不影响接下来的判断
            else:
                s1=s#否则不对字符串进行变化
        #对处理完成的字符串进行遍历，遇到数字将其放入新的字符串，遇到第一个不是数字的字符即停止遍历
        for i in range(len(s1)):
            if s1[i] in l1:
                s2+=s1[i]
            else:
                break
        #如果遍历结束的数组为空，则返回0
        if s2=='':
            return 0
        #如果存在数字，则将字符串转换为原来的数字并添加上正负号
        s2=int(s2)*flag
        #判断范围，超过范围则截至到范围，不超过范围则输出本身
        if s2>=(2**31)-1:
            return (2**31)-1
        elif s2<=-(2**31):
            return -(2**31)
        else:
            return s2
