#https://leetcode.cn/problems/longest-common-prefix/description/
'''
解题思路：
如果输出的数组中存在空字符串，那最大的公共前缀就是空
否则的话，先取数组中的第一个字符串为模板，将其与其它的字符串进行对比。
匹配上了，则弹出字符串与下一个字符串对比；如果没对比上，但是确实存在公共前缀，则不断削减模板字符串的末尾字符，以求匹配上。
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs:#如果输出的数组中存在空字符串，那最大的公共前缀就是空
            return ''
        result=strs[0]#取数组中的第一个字符串为模板
        strs=strs[1:]#将模板字符串进行弹出
        while strs:#不断遍历字符串列表，直到所有的列表遍历完成
            if len(result)>0:#模板非空，继续遍历
                if result[0]==strs[0][0]:#是否存在最低限度的公共前缀
                    if result == strs[0][0:len(result)]:#查看当前模板是否是最大公共前缀
                        strs=strs[1:]#是的话就对下一个字符串进行遍历
                    else:
                        result=result[:-1]#不是，则缩减模板字符串
                else:
                    return ''
            else:
                return ''
        return result
