#https://leetcode.cn/problems/combination-sum/
'''
解题思路：采用回溯的思路，但是因为可以有重复的元素，所以index不必加1，因为不需要重复的答案，所以将path的排序元素是否在result进行判断。
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]# 初始化一个空列表，用于存放所有可能的组合。
        def dfs(candidates,target,index,currentSum,path,result):
            if currentSum>target:#如果当前的和currentSum已经超过了目标和targetSum，就没有必要继续搜索，因为不可能通过添加更多的数字来减小当前的和。
                return
            if currentSum==target:#如果path中的和等于目标值
                path1=sorted(path)#对其进行排序，并创建新数组进行储存
                if path1 not in result:#取出重复结果列表
                    result.append(path1[:])
                    return 
            for i in range(index,len(candidates)):#从startIndex开始不断遍历
                currentSum+=candidates[i]#计算总和
                path.append(candidates[i])#数组元素进行列表
                dfs(candidates,target,index,currentSum,path,result)#回溯
                currentSum-=candidates[i]#回溯步骤，从当前和中减去当前的元素。
                path.pop()#回溯步骤，从路径中移除最后一个数字。
        dfs(candidates,target,0,0,[],result)#调用回溯函数
        return result
