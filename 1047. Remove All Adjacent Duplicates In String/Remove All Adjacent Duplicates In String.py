#https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/
'''
解题思路：采用栈的思想，先将元素入栈，然后判断将要入栈的元素与栈顶元素是否相同，如果相同，则栈顶元素弹出，否则元素入栈。
'''
class Solution:
    def removeDuplicates(self, s: str) -> str:
        s=list(s)#先将字符串列表化
        res=[]#创建一个空战
        for i in range(len(s)):#遍历列表
            if res and res[-1]==s[i]:#如果栈非空且栈顶元素等于当前遍历元素
                res.pop()#栈顶元素弹出
            else:
                res.append(s[i])#否则元素入栈
        res=''.join(res)#将列表转回字符串
        return res
