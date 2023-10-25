#https://leetcode.cn/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if '' in strs:
            return ''
        result=strs[0]
        strs=strs[1:]
        while strs:
            if len(result)>0:
                if result[0]==strs[0][0]:
                    if result == strs[0][0:len(result)]:
                        strs=strs[1:]
                    else:
                        result=result[:-1]
                else:
                    return ''
            else:
                return ''
        return result
