#https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/
'''
解题思路：采用贪心算法，局部最优解是每次取反数据中的最小值，这样能使得数组的和的数值下降最小（最小值为正数）或者增加最大（最小值为负数）。
'''
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k:#不断取反，直到达到指定数值
            minValue=min(nums)#寻找数组最小值
            index=nums.index(minValue)#找到数组最小值的下标
            nums[index]=-nums[index]#将最小值取反
            k-=1#取反次数减一
        return sum(nums)#返回数组和
