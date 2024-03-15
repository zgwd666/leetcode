#https://leetcode.cn/problems/backspace-string-compare/
'''
解题思路：
采用移除数组元素的思路配合双指针的使用。
具体为：对两个数组分别进行一次移除元素的操作，定义slow和fast指针，fast遍历整个数组，碰到非#元素进行slow+1操作，即将元素覆盖操作。如果碰到#元素，执行slow-1操作，也就是元素回退操作。如果回退到0，就不能往回退，数组长度不能为负数。
然后将两个移除数组元素的数组进行比较即可。
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        slows=0#定义s字符串的慢指针
        slowt=0#定义t字符串的慢指针
        s=list(s)#将s字符串列表化
        t=list(t)#将t字符串列表化
        m,n=len(s),len(t)#获取s t长度
        for fast in range(m):#对s字符串进行遍历
            if s[fast]!='#':#碰到非#元素赋值给slows下标，slows+1
                s[slows]=s[fast]
                slows+=1
            if s[fast]=='#' and (slows>0):#碰到#元素且slows大于0，则回退
                slows-=1
        for fast in range(n):#对t字符串进行遍历
            if t[fast]!='#':#碰到非#元素赋值给slowt下标，slowt+1
                t[slowt]=t[fast]
                slowt+=1
            if t[fast]=='#' and slowt>0:#碰到#元素且slows大于0，则回退
                slowt-=1
        if s[:slows]==t[:slowt]:#对比处理完成的s和t字符，相等则返回Ture
            return True
        return False#否则返回False
