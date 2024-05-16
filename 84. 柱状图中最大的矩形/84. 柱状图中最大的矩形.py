#https://leetcode.cn/problems/largest-rectangle-in-histogram/
'''
解题思路：
本题是要找每个柱子左右两边第一个小于该柱子的柱子，所以从栈头（元素从栈头弹出）到栈顶的顺序应该是从大到小的顺序
只有栈里从大到小的顺序，才能保证栈顶元素找到左右两边第一个小于栈顶元素的柱子。
其实就是栈顶和栈顶的下一个元素以及要入栈的三个元素组成了我们要求最大面积的宽度和高度。
主要就是分析清楚如下三种情况：
- 情况一：当前遍历的元素heights[i]大于栈顶元素heights[st.top()]的情况
- 情况二：当前遍历的元素heights[i]等于栈顶元素heights[st.top()]的情况
- 情况三：当前遍历的元素heights[i]小于栈顶元素heights[st.top()]的情况
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==1:#判断特殊情况
            return heights[0]
        stack=[0]#初始化栈
        result=0#初始化结果
          # 输入数组首尾各补上一个0（本题原首尾的两个柱子可以作为核心柱进行最大面积尝试
        heights.insert(0,0)
        heights.append(0)
        #进行遍历
        for i in range(1,len(heights)):
            if heights[i]>heights[stack[-1]]:
                stack.append(i)
            elif heights[i]==heights[stack[-1]]:
                stack[-1]=i
            else:
                while stack and heights[i]<heights[stack[-1]]:
                    mid=stack[-1]
                    stack.pop()
                    if stack:#根据公式进行计算
                        w=i-stack[-1]-1
                        h=heights[mid]
                        result=max(w*h,result)
                stack.append(i)
        return result
