#https://leetcode.cn/problems/container-with-most-water/description/
'''
解题思路：
盛水的量等于二者之间的距离和二者最小值的乘积。
对于初始状态，此时二者为下标为i=0,j=len(height)-1；高度分别为height[i],height[j]
假设min_height=min(height[i],height[j])，max_height=max(height[i],height[j])
如果向内移动max_height对应的下标，则会导致j-i变小，min_height可能不变或变小，总体的结果一定变小
如果向内移动min_height对应的下标，则会导致j-i变小，min_height可能不变或变小或变大，总体的结果可能会变大
所以每次移动的必须是短边，移动后将新的盛水量与原先的进行对比，不断更新盛水的量，直到i=j为止
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1#初始化i,j的状态
        sum=0#初始化最大盛水量
        #进行遍历
        while i<j:
            cur_sum=(j-i)*min(height[i],height[j])#计算当前下标下的盛水量
            if sum<cur_sum:#将新的盛水量与原先的进行对比，不断更新盛水的量
                sum=cur_sum
            if height[i]<height[j]:#移动短边的下标
                i+=1
            else:
                j-=1
        return sum
