#https://leetcode.cn/problems/permutations/
'''
解题思路：采用回溯进行一个个的枚举，需要使用used数组进行避免重复元素选取的操作
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]#初始化结果列表
        used=[False for  _ in range(len(nums))]#初始化used数组避免进行重复元素的选取
        def dfs(nums,path,used,result):#回溯函数
            if len(path)==len(nums):#当列表中的元素和原本数组中的元素个数一致时
                result.append(path[:])#添加到结果中
                return
            for i in range(len(nums)):#进行循环
                if not used[i]:#如果当前元素未被使用
                    used[i]=True#将当前元素标记为已使用
                    path.append(nums[i])#数组中添加当前元素
                    dfs(nums,path,used,result)#进行回溯
                    used[i]=False#回溯结束，恢复当前元素的未被使用状态
                    path.pop()#弹出元素
        dfs(nums,[],used,result)#进行回溯
        return result#返回结果s
