#https://leetcode.cn/problems/rotate-array/description/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：采用一个很简答的想法，每次转向都是讲数组的最后一个元素放到第一个位置上，
那么就可以每次讲最后一个元素弹出，然后insert第0个位置
时间复杂度为O(n)，空间复杂度也为O(n)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):#轮转k次
            temp_last=nums.pop()#弹出最后一个元素
            nums.insert(0,temp_last)#讲弹出的元素放到下标为0的位置
