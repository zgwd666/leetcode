#https://leetcode.cn/problems/jump-game-ii/
'''
解题思路对于每一个位置 i 来说，所能跳到的所有位置都可以作为下一个起跳点，为了尽可能使用最少的跳跃次数，所以我们应该使得下一次起跳所能达到的位置尽可能的远。简单来说，就是每次在「可跳范围」内选择可以使下一次跳的更远的位置。这样才能获得最少跳跃次数。、
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:#判断特殊情况
            return 0
        cover=0# 下一步覆盖最远距离下标
        end=0 # 当前覆盖最远距离下标
        steps=0 # 记录走的最大步数
        for i in range(len(nums)):
            cover=max(nums[i]+i,cover)#更新下一步覆盖最远距离下标
            if i==end: # 遇到当前覆盖最远距离下标
                end=cover # 更新当前覆盖最远距离下标
                steps+=1# 需要走下一步
                if cover>=len(nums)-1: #当前覆盖最远距离达到数组末尾，不用再做ans++操作，直接结束
                    break
        return steps
