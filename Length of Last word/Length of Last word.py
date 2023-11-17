'''
解题思路：先将字符串的右侧空格去除，然后从右向前遍历，遇到空格，跳出遍历。
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()#将字符串的左右两侧的空格全部去除
        r=len(s)-1#定义右指针初始位置
        maxlength=0#初始化最大长度
        while r>=0:#当右指针超出最左侧跳出遍历
            if s[r]!=' ':#遇到字符，长度加1
                maxlength+=1
                r-=1
            else:#遇到空格，遍历跳出
                break
        return maxlength#返回最大长度
