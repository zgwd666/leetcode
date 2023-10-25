#https://leetcode.cn/problems/palindrome-number/description/
'''
解题思路：
如果是负数，负号的存在使其，根本就不可能是回文数，所以无需管正负号，直接转换为字符串，倒转后，看与原字符串是否一致。是则表示是回文数，否则表示不是回文数。
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #将数字转换为字符串
        x_str=str(x)
        #将字符串反转
        x_str1=x_str[::-1]
        #将反转后的字符串与原字符串进行对比，如二者相等，则为回文数，否则不是
        if x_str==x_str1:
            return True
        else:
            return False
