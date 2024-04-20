#https://leetcode.cn/problems/non-decreasing-subsequences/
'''
解题思路：采用回溯的思路，结束条件为数组中存在两个及以上的元素且呈现非递减的态势
'''
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]#初始化结果
        def dfs(nums,index,path,result):#回溯函数
            if len(path)>=2:#当列表中存在两个及以上元素时开始判断
                if path[-1]<path[-2] or path in result:#当不符合非递减或者重复直接返回
                    return
                else:#符合要求存入结果列表中
                    result.append(path[:])
            for i in range(index,len(nums)):#进行遍历回溯
                path.append(nums[i])
                dfs(nums,i+1,path,result)
                path.pop()
        dfs(nums,0,[],result)#开始回溯
        return results
