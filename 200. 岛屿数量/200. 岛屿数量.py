#https://leetcode.cn/problems/number-of-islands/
'''
解题思路：
采用BFS的解法

题目的意思是每座岛屿只能由水平方向/竖直方向上相邻的陆地连接形成。

也就是说斜角度连接的就是两个岛屿了。

本题的具体思路，是用遇到一个没有遍历过的节点陆地，计数器就加一，然后把该节点陆地所能遍历到的陆地都标记上。

在之后的遍历中，如果遇到标记过的陆地节点和海洋节点直接跳过，这样计数器就是最终岛屿的数量。
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)#得到m
        dir=[(0,1),(1,0),(0,-1),(-1,0)]#创建方向数组
        n=len(grid[0])#得到n
        visited=[[False for i in range(n)]for i in range(m)]#初始化标记数组
        res=0#初始化结果
        def dfs(grid,visited,x,y):#进行bfs，参数时网格数组，标识数组，当前点的坐标
            queue=[]#初始化队列
            queue.append((x,y))#将当前点加入到队列中
            visited[x][y]=True#将当前点标记为已遍历
            while queue:#进行遍历
                curx,cury=queue.pop(0)#弹出队头的坐标作为当前坐标
                for dx,dy in dir:#对当前点的四个方向进行遍历
                    nextx,nexty=curx+dx,cury+dy#计算当前点
                    if nextx<0 or nextx>=m or nexty<0 or nexty>=n or grid[nextx][nexty]=='0' or visited[nextx][nexty]:#如果当前点超过范围或者网格值为0或者已经遍历过，则跳过当前点
                        continue
                    visited[nextx][nexty]=True#将当前点标识为已遍历
                    queue.append((nextx,nexty))#将当前点加入队列中
        for i in range(m):#对格网中每一个点进行遍历
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':#如果当前点没有被遍历且值为1
                    res+=1#结果加一
                    dfs(grid,visited,i,j)#将本岛的所有节点都进行标记
        return res#返回结果
