#https://leetcode.cn/problems/repeated-substring-pattern/
'''
解题思路：假设s可以由子串x重复n次构成，则有2s可以由x重复2n构成，去除子串的首尾字符，此时其中x的重复次数为2n-2次。
这时如果s在去除首尾元素的2s子串中，就证明2n-2>=n，即n>=2，也就是s可以由x重复2次以上组成
否则，n<2，n为正整数，n为1，说明n不存在比自己更小的重复子串
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
