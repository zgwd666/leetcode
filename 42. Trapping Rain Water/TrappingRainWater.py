#https://leetcode.cn/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：接雨水类似于木桶效应，在某位置能接到的雨水数量等于最短的边减去本位置的值
具体就是该位置接到雨水的数量等于左边最大值和右边最大值中的最小值减去该位置的值
本题采用双指针的思想，具体为：
定义左指针，用来探究左指针所处地及其左侧最大值
定义右指针，用来探究右指针所处地及其左侧最大值
因为短板效应，所以取左右最大值中的最小值减去较小指标处于的位置并进行累加，计算结果
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)#求出数组总长度
        ans=0#初始化结果
        left=0#初始化做指标
        right=n-1#初始化右指标
        leftMax=rightMax=0#初始化左右指标最大值
        while left<right:#进行遍历，停止条件是左指标超过右值标
           leftMax=max(leftMax,height[left])#计算左指标左侧及本身最大值
           rightMax=max(rightMax,height[right])#计算右指标右侧及本身最大值
           if leftMax <rightMax:#如果左边最大值较小，可以对左指标处进行短板效应的计算
               ans+=leftMax-height[left]#结果等于左侧最大值减去本位置的值
               left+=1#左指标右移
           else:#如果右边最大值较小，可以对右指标处进行短板效应的计算
                ans+=rightMax-height[right]#结果等于右侧最大值减去本位置的值
                right-=1#右值标左移
        return ans#返回结果
