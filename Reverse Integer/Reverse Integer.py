#https://leetcode.cn/problems/reverse-integer/description/
'''
解题思路：
将整数无论正负先转换成正数，然后转换成字符串，进行字符串的反转，最后转回整数，添加上正负号即可
'''
class Solution:
    def reverse(self, x: int) -> int:
        #如果是0，那就直接返回0
        if x==0:
            return 0
        #如果是负数
        if x<0:
            x=abs(x)#先转换成正数
            x=str(x)#转换为字符串
            x=x[::-1]#字符串反转
            if -int(x)<-(2**31):#判断范围，超过范围，输出0
                return 0
            else:#不超过范围，输出反转后字符串的int，再加上负号
                return -int(x)

        else:#如果是正数
            x=str(x)#转换为字符串
            x=x[::-1]#字符串反转
            if int(x)>(2**31)-1:#判断范围，超过范围，输出0
                return 0
            else:#不超过范围，输出反转后字符串的int
                return int(x) 
