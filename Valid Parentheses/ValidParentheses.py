#https://leetcode.cn/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        输入：
        str：输入的括号字符串
        输出：
        是否是成对有效字符串
        '''
        str=list(s)#将字符串列表化
        dict_Parentheses={'(':')','{':'}','[':']'}#创建匹配字典
        #如果输入的字符串是单数的，那肯定不是配对的，直接输出false
        if length%2!=0:
            return False
        #当输入的字符串是双数的，进入下一阶段的判断
        else:
            #创建一个空栈
            stack=[]
            #对字符串中的元素进行遍历
            for i in str:
                #当字符串中元素是括号的左半边时，将其入栈
                if i in dict_Parentheses:
                    stack.append(i)
                #否则当字符串中元素不是括号的左边且不是空栈：
                elif stack!=[]:
                    #对stack进行出栈操作，先出栈之后才进行判断操作，所示无论是否与右半边进行匹配，都完成出栈操作。
                    #如果出栈的元素与本轮遍历的元素不是匹配的括号则直接返回False，否则出栈后，进行下一轮遍历。
                    if dict_Parentheses[stack.pop()]!=i:
                        return False
                #否则当字符串中元素不是括号的左边且是空栈，这证输入的第一个元素就是括号的右半边，直接返回False：
                else :
                    return False
            #最后看栈中元素是否全部出完，也就是是否完全匹配上，防止一连三个进栈，只出一个元素的等情况的发生。
            return len(stack)==0
