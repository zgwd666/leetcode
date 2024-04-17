#https://leetcode.cn/problems/combination-sum-iii/
'''
解题思路：使用回溯算法来寻找所有可能的组合，这些组合由1到9之间的整数构成，且数量为k个，总和为n。从`startIndex`（默认为1）开始，逐步尝试每个数字，将其加入到当前路径中，并递归地继续搜索直到找到满足条件的组合或达到搜索的边界。在每一步递归中，都会检查当前路径的长度和当前和是否满足题目要求，如果满足则将当前路径的副本添加到结果集中。为了避免无效搜索，当当前和超过目标和或路径长度达到k时，会剪枝停止搜索。通过这种方式，算法能够探索所有可能的组合，并高效地构建出所有满足条件的组合列表。
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]# 初始化一个空列表，用于存放所有可能的组合。
        def dfs(k,n,index,path,result,currentSum):
            if currentSum>n:#如果当前的和currentSum已经超过了目标和targetSum，就没有必要继续搜索，因为不可能通过添加更多的数字来减小当前的和。
                return 
            if len(path)==k and currentSum==n:#如果当前的长度等于k且值等于n，将当前路径（组合）添加到结果列表中
                result.append(path[:])
            for i in range(index,9-(k-len(path))+2):#这是一个循环，用于尝试从startIndex开始的所有可能的数字。循环的结束条件是9 - (k - len(path)) + 2，这是为了确保在剩余的数字中有足够的空间放置剩余的k - len(path)个数字。
                path.append(i)#将当前数字i添加到路径中
                currentSum+=i# 将当前数字i加到当前和currentSum中。
                dfs(k,n,i+1,path,result,currentSum)#递归调用
                path.pop()#回溯步骤，从路径中移除最后一个数字。
                currentSum-=i#回溯步骤，从当前和中减去i。
        dfs(k,n,1,[],result,0)#调用回溯函数
        return result
