#https://leetcode.cn/problems/permutations-ii/
'''
解题思路：采用回溯进行一个个的枚举，需要使用used数组进行避免重复元素选取的操作，再添加一个判断是否重复的过程
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]#初始化结果列表
        used=[False]*len(nums)#初始化used数组避免进行重复元素的选取
        def dfs(nums,used,path,result):#回溯函数
            if len(path)==len(nums):#当列表中的元素和原本数组中的元素个数一致时
                if path not in result:#当前排列未出现过时
                    result.append(path[:])#添加到结果中
                return
            for i in range(len(nums)):#进行循环
                if not used[i]:#如果当前元素未被使用
                    used[i]=True#将当前元素标记为已使
                    path.append(nums[i])#数组中添加当前元素
                    dfs(nums,used,path,result)#进行回溯
                    path.pop()#弹出元素
                    used[i]=False#回溯结束，恢复当前元素的未被使用状态
        dfs(nums,used,[],result)#进行回溯
        return result#返回结果s
