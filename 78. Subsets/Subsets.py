#https://leetcode.cn/problems/subsets/
'''
解题思路：这个算法利用了回溯法的思想，通过递归和回溯来生成所有可能的子集。它首先尝试添加当前索引的元素，然后递归地尝试所有后续索引的元素，直到所有可能的组合都被探索完毕。
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]#result被初始化为一个包含空列表的列表，因为空列表也是一个有效的子集
        nums.sort()#nums.sort()对输入的列表nums进行排序。排序是生成所有子集的一个常用步骤，因为它可以简化子集的生成过程。
        #dfs是一个深度优先搜索（Depth-First Search, DFS）的递归函数，用于生成所有可能的子集。
        def dfs(nums,index,path,result):
            #如果path非空，那么它代表了一个有效的子集，将其添加到result中
            if path:
                result.append(path[:])
            #使用一个for循环从当前索引index开始遍历nums，直到列表的末尾
            for i in range(index,len(nums)):
                #在每次迭代中，将当前索引的数字添加到path中，然后递归调用dfs函数，递归的下一个索引设置为当前索引加1。
                path.append(nums[i])
                dfs(nums,i+1,path,result)
                #在递归调用之后，执行path.pop()以移除path中的最后一个元素，这是回溯过程的一部分，它允许函数返回到上一个状态并继续探索其他可能的子集。
                path.pop()
        #在dfs函数定义之后，使用dfs(nums, 0, [], result)开始递归过程，从索引0开始，初始路径为空。
        dfs(nums,0,[],result)
        return result
