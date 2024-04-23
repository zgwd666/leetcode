#https://leetcode.cn/problems/wiggle-subsequence/
'''
解题思路：本题的局部最优解为删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就有两个局部峰值。全局最优解为整个序列有最多的局部峰值。实际操作上，只需要统计数组的峰值数量就可以。
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<2:return len(nums)#当数组中的元素个数小于2时，摇摆序列的数量就是多少
        curdiff=0#当前差值
        prediff=0#之前差值
        count=1#记录峰值的个数，初始为1（默认最右边的元素被视为峰值）
        for i in range(len(nums)-1):#进行遍历
            curdiff=nums[i+1]-nums[i]#计算当前差值
            if curdiff:#跳过相同的元素
                if curdiff*prediff<=0:#如果得到一个峰值
                    count+=1#计数加一
                prediff=curdiff#将当前的差值赋给之前差值
        return count#返回计数
