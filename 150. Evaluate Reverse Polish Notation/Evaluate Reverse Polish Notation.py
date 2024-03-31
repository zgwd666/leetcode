#https://leetcode.cn/problems/evaluate-reverse-polish-notation/
'''
解题思路：遇到数字进栈，遇到字符就将栈顶的两个元素弹出，并按照指定的运算符进行计算
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp=[]#定义一个栈
        for i in tokens:#遍历字符串
            if i not in ['+','-','*','/']:#如果遍历的元素不是运算符
                temp.append(int(i))#则将数字映射为整数入栈
            else:#如果遍历到运算符
                a=temp.pop()#弹出栈顶第一个元素
                b=temp.pop()#弹出栈顶第二个元素
                #根据运算符进行对应的运算，注意是b运算符a
                if i=='+':
                    temp.append(b+a)
                if i=='-':
                    temp.append(b-a)
                if i=='*':
                    temp.append(b*a)
                if i=='/':
                    temp.append(int(b/a))
        return temp[-1]#返回最后的计算结果
