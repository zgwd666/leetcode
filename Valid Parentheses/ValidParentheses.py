#https://leetcode.cn/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        length=len(s)
        str=list(s)
        dict_Parentheses={'(':')','{':'}','[':']'}
        if length%2!=0:
            return False
        else:
            stack=[]
            for i in str:
                if i in dict_Parentheses:
                    stack.append(i)
                elif stack!=[]:
                    if dict_Parentheses[stack.pop()]!=i:
                        return False
                else :
                    return False
            return len(stack)==0
