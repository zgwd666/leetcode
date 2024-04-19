#https://leetcode.cn/problems/combination-sum-ii/
'''
解题思路：采用回溯的思路，为了使得结果不重复，就需要将原始的数组进行排序，在回溯的循环中跳过相同元素即可。

'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]# 初始化一个空列表，用于存放所有可能的组合。
        candidates.sort()#数组排序
        def dfs(candidates,target,index,path,result):
            if target==0:#判断结束条件，如果target等于0，则将path添加到结果列表中
                result.append(path[:])
            for i in range(index,len(candidates)):#进行循环
                if i>index and candidates[i]==candidates[i-1]:#判断是否为重复元素，跳过重复元素，避免重复的组合
                    continue
                if candidates[i]>target:#如果之后的元素都大于剩下的值，则直接跳出本次训话
                    break
                path.append(candidates[i])#将元素添加到列表中
                dfs(candidates,target-candidates[i],i+1,path,result)#进行回溯，为了避免元素复用，采用i+1
                path.pop()#回溯步骤，从路径中移除最后一个数字。
        dfs(candidates,target,0,[],result)#调用回溯函数
        return result
