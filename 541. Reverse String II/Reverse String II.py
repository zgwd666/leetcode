#https://leetcode.cn/problems/reverse-string-ii/
'''
解题思路：每2k个字符进行一次操作，那么在循环的时候以2k为步长进行
题目的意思是在每个2k中，前k个都是需要反转的。
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)#将字符转换为数组，方便反转操作
        for i in range(0,len(s),2*k):#进行遍历，以2k为步长
            if i+k<=len(s):#当2k个中前k个字符未超过字符串，则前k个反转
                s[i:i+k] = s[i:i+k][::-1]
            else:#如果最后剩下来的不足k个，则剩下整体反转
                s[i:]=s[i:][::-1]
        s=''.join(s)#将数组转回字符
        return s
