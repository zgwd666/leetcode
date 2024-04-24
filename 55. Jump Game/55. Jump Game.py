#https://leetcode.cn/problems/jump-game/
'''
解题思路：每次移动取最大跳跃步数（得到最大的覆盖范围），每移动一个单位，就更新最大覆盖范围。
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:#当数组中仅有一个元素时，一定可以到达
            return True
        cover=0#初始化最大覆盖范围
        i=0#初始化下标
        while i<=cover:#当最大覆盖范围能覆盖到当前下标继续遍历，否则就直接中断遍历
            cover=max(cover,i+nums[i])#更新最大覆盖范围
            if cover>=len(nums)-1:#判断是否已经覆盖到末尾
                return True
            i+=1#下标向前移动
        return False#当最大覆盖范围无法覆盖到末尾，返回Falses
