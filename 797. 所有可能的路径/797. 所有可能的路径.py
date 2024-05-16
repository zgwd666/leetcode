#https://leetcode.cn/problems/all-paths-from-source-to-target/
'''
解题思路：
1.确定递归函数、参数

首先dfs一定要存一个图，用来遍历的，还有存一个我们目前的节点

至于单一路径，和路径集合可以放在全局变量

2.确认终止条件

当目前遍历的节点为最后一个节点的时候，就找到了一条，从出发点到终止点的路径

3.处理目前搜索出来的路径

接下来是走当前遍历节点x的下一个节点

首先是要找到x节点链接到哪些节点
接下来就是将选中的x所连接的节点，加入到单一路径来
进入下一层递归
最后就是回溯的过程
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path=[0]#初始化path
        result=[]#初始化结果
        def dfs(graph,x):#进行dfs，参数是图和当前节点
            if x==len(graph)-1:#当前节点等于终点
                result.append(path[:])#结果添加
                return#返回结果
            for i in range(len(graph[x])):#遍历当前节点的链接节点
                path.append(graph[x][i])#接下来就是将选中的x所连接的节点，加入到单一路径来
                dfs(graph,graph[x][i])#进入下一层递归
                path.pop()#最后就是回溯的过程
        dfs(graph,0)#进行dfs
        return result#返回结果
