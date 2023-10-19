#https://leetcode.cn/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        输入：
        nums:输入的数组
        target：目标值
        输出：
        [i,j]：满足加和等于目标值的数组下标
        '''
        self.num=nums
        self.target=target
        #进行循环遍历
        for i in range(len(self.num)):
            for j in range(i+1,len(self.num)):
                if self.num[i]+self.num[j]==self.target:
                    return [i,j]
                j+=1
            i+=1
        return [i,j]
