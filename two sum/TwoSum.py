#https://leetcode.cn/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.num=nums
        self.target=target
        for i in range(len(self.num)):
            for j in range(i+1,len(self.num)):
                if self.num[i]+self.num[j]==self.target:
                    return [i,j]
                j+=1
            i+=1
        return [i,j]
