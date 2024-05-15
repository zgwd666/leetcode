#https://leetcode.cn/problems/trapping-rain-water/
'''
解题思路：
使用单调栈，是通过长*宽来计算雨水面积的。

长是通过柱子的高度来计算的，宽是通过柱子之间的下标来计算的。

单调栈的处理逻辑主要有如下的三种情况

- 情况一：当前遍历的元素（柱子）高度小于栈顶元素的高度 height[i] < height[st.top()]
- 情况二：当前遍历的元素（柱子）高度等于栈顶元素的高度 height[i] == height[st.top()]
- 情况三：当前遍历的元素（柱子）高度大于栈顶元素的高度 height[i] > height[st.top()]

先将下标0的柱子加入栈中，=。栈中存放我们遍历过的元素，所以先将下标0加进来。

然后从下标1开始遍历所有的柱子

如果当前遍历的元素（柱子）高度小于栈顶元素的高度，就把这个元素加入栈中，因为栈里本来就要保持从小到大是顺序（从栈头到栈顶）

如果当前遍历的元素（柱子）高度等于栈顶元素的高度，需要更新栈顶元素，因为遇到相同高度的柱子，需要使用最右边的柱子来计算宽度

如果当前遍历的元素（柱子）高度大于栈顶元素的高度，此时就出现了凹槽，取栈顶元素，将栈顶元素弹出，这个就是凹槽的底部，也就是中间位置，下标记为mid，对应的高度为height[mid]

此时栈顶的元素st.top()，就是凹槽左边的位置，下标为st.top()，对应的高度为height[st.top()]，此时遍历的元素i，就是凹槽右边的位置，下标为i，对用的高度为height[i]

其实就是利用栈顶和栈顶的下一个元素以及要入栈的元素，三个元素来接水

那么雨水的高度就是min(凹槽左边高度，凹槽右边高度)-凹槽底部高度

雨水的宽度就是凹槽右边的下标-凹槽左边的下标-1（因为只需要求中间的宽度，两边是栏杆）

此时凹槽雨水的体积为高度*宽度。
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<2:#判断特殊情况
            return 0
        result=0#初始化结果
        stack=[0]#初始化栈
        for i in range(1,len(height)):#进行判断
            if height[i]<height[stack[-1]]:#当前元素小于以栈顶元素为下标的元素时，将当前元素的下标加入栈顶
                stack.append(i)
            elif height[i]==height[stack[-1]]:#等于就更新下标
                stack[-1]=i
            else:#当前元素大于以栈顶元素为下标的元素时
                while stack and height[i]>height[stack[-1]]:#对栈进行遍历直到栈为空或者当前元素不大于以栈顶元素为下标的元素时
                    mid=height[stack[-1]]#获取凹槽底部
                    stack.pop()#将该下标弹出
                    if stack:#如果此时还存在左边界
                        h=min(height[i],height[stack[-1]])-mid#计算高度
                        w=i-stack[-1]-1#计算宽度
                        result+=w*h#计算体积
                stack.append(i)  #遍历完成，将当前元素的下标加入栈顶       
        return result#返回结果
