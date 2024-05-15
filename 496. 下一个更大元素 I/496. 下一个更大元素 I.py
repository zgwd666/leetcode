#https://leetcode.cn/problems/next-greater-element-i/
'''
解题思路：采用单调栈的方式，先把num2中的每个元素的右侧第一个比当前元素大的元素记录下来，然后根据nums1在nums2中的索引取出相应的元素存放到结果元素中即可
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #先通过单调栈的方式求出每个元素右侧第一个比自己大的元素
        temp=[-1]*len(nums2)#初始化存放元素数组
        stack=[0]#初始化栈
        for i in range(1,len(nums2)):#进行遍历
            if nums2[i]<=nums2[stack[-1]]:#当前元素不大于以栈顶元素为下标的元素时，将当前元素的下标加入栈顶
                stack.append(i)
            else:#当前元素大于以栈顶元素为下标的元素时
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:#对栈进行遍历直到栈为空或者当前元素不大于以栈顶元素为下标的元素时
                    temp[stack[-1]]=nums2[i]#赋值
                    stack.pop()#将栈顶元素弹出
                stack.append(i)#遍历完成，将当前元素的下标加入栈顶
        result=[]#初始化结果数组
        for i in range(len(nums1)):#对第一个数组元素进行遍历
            index=nums2.index(nums1[i])#找到对应的索引
            result.append(temp[index])#根据索引提取元素
        return result#返回结果
