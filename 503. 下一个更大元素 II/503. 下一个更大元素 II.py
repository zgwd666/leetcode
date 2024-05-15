#https://leetcode.cn/problems/next-greater-element-ii/
'''
解题思路：根据题目的意思可以发现，两个数组拼在一起就可以实现循环数组的效果。然后对二倍数组采用单调栈计算每个元素右侧第一个大于本元素的元素，最后输出的时候截取前一半就可以

'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums)==1:#判断特殊情况
            return [-1]
        temp=nums*2#将两个数组拼起来
        result=[-1]*len(temp)#初始化结果数组
        stack=[0]#初始化栈
        for i in range(1,len(temp)):#进行遍历
            if temp[i]<=temp[stack[-1]]:#当前元素不大于以栈顶元素为下标的元素时，将当前元素的下标加入栈顶
                stack.append(i)
            else:#当前元素大于以栈顶元素为下标的元素时
                while stack and temp[i]>temp[stack[-1]]:#对栈进行遍历直到栈为空或者当前元素不大于以栈顶元素为下标的元素时
                    result[stack[-1]]=temp[i]#赋值
                    stack.pop()#将栈顶元素弹出
                stack.append(i)#遍历完成，将当前元素的下标加入栈顶
        return result[:len(nums)]#返回前一半的结果即可
