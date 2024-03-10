#https://leetcode.cn/problems/subarray-sum-equals-k/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
采用前缀和和hashmap的思想
具体来说就是分别求解每个位置前面元素加上本身的和，然后减去目标值，看剩下的值是否存在hashmap中，及存在的个数。
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        temp={}#定义hashmap
        tempSum=0#初始化前缀和
        ans=0#初始化结果
        temp[0]=1#前缀和先添加一个0，作为相减为0的预备
        for i in range(len(nums)):#进行遍历
            tempSum+=nums[i]#计算前缀和
            if tempSum-k in temp:#如果前缀和减去k在hashmap中
                ans+=temp[tempSum-k]#前面有多少组就能组成多少个子数组
            if tempSum not in temp:#不存在，创建并赋值为1
                temp[tempSum]=1
            else:#否则加1
                temp[tempSum]+=1

        return ans
