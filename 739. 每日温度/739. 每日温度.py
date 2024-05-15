#https://leetcode.cn/problems/daily-temperatures/
'''
解题思路：采用单调栈存放元素的下标，当前遍历的元素小于等于以栈顶元素为下标的元素的时候，将当前元素的下标加入栈顶，否则的话，不断的弹出栈顶元素的下标，直到不大于为止，此时加当前元素的下标加入栈顶。
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)==1:#判断特殊情况
            return [0]
        result=[0]*len(temperatures)#初始化结果数组
        stack=[0]#初始化栈
        for i in range(1,len(temperatures)):#进行遍历
            if temperatures[i]<=temperatures[stack[-1]]:#当前元素不大于以栈顶元素为下标的元素时，将当前元素的下标加入栈顶
                stack.append(i)
            else:##当前元素大于以栈顶元素为下标的元素时
                while len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]:#对栈进行遍历直到栈为空或者当前元素不大于以栈顶元素为下标的元素时
                    result[stack[-1]]=i-stack[-1]#计算距离
                    stack.pop()#将栈顶元素弹出
                stack.append(i)#遍历完成，将当前元素的下标加入栈顶
        return result#返回结果
