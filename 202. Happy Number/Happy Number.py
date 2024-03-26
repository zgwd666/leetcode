#https://leetcode.cn/problems/happy-number/
'''
解题思路：目中说了会无限循环，无限循环就代表着在求和的过程中，sum的值会重复出现。
也就是说在循环过程中，出现了重复的sum，就可以判断到不了，也就可以直接返回False。
对每个位置数字上的取用可以将其转换为字符串，在把每个字符映射到int就可以
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        dict1={}#定义一个字典，作为hash表
        while True:#进行遍历
            theSum=0#初始化和
            if n not in dict1:#存储n
                dict1[n]=1
            else:#当n第二次出现，证明进入循环，也就是永远到不了
                return False
            n=str(n)#将数字转换为字符串
            for i in n:#取出每个字符，将其转换为int，求平方
                theSum+=int(i)**2
            n=theSum#将sum赋值给n
            if n==1:#如果和为，返回True
                return True 
