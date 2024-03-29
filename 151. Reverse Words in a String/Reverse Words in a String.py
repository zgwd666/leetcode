#https://leetcode.cn/problems/reverse-words-in-a-string/
'''
解题思路：先将字符串拆解为数组元素，然后定义双指针相向而行，在过程中交换。
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()#将字符串拆分为数组，其中所有的空格都被删除
        l,r=0,len(s)-1#定义左右指针，指向数组的开头和末尾元素
        while l<r:#进行遍历
            s[l],s[r]=s[r],s[l]#交换头尾元素
            l+=1#左指针右移
            r-=1#右指针左移
        s=' '.join(s)#将数组元素还原回字符串，中间用空格连接
        return s
