#https://leetcode.cn/problems/combinations/
'''
解题思路：采用回溯的算法进行计算
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]#初始化结果
        def dfs(n,k,index,path,result):定义一个嵌套的dfs函数，用于执行深度优先搜索
            if len(path)==k:#表示已经找到了一个长度为k的组合，将其添加到结果集中
                result.append(path[:])
            for i in range(index,n+1):#从startIndex开始不断遍历
                path.append(i)
                dfs(n,k,i+1,path,result)
                path.pop()
        dfs(n,k,1,[],result)#执行回溯算法
        return result#返回结果
