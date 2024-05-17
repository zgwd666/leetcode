#https://leetcode.cn/problems/max-area-of-island/
'''
解题思路：
采用BFS的思路

题目的意思是每座岛屿只能由水平方向/竖直方向上相邻的陆地连接形成。

也就是说斜角度连接的就是两个岛屿了。

本题的具体思路，是用遇到一个没有遍历过的节点陆地，就对该岛屿进行遍历，计算面积也就是计算该岛屿由几个元素组成，然后求出最大的岛屿即可。

在之后的遍历中，如果遇到标记过的陆地节点和海洋节点直接跳过，这样计数器就是最大岛屿的面积。
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)#得到m
        n=len(grid[0])#得到n
        dir=[(0,1),(1,0),(0,-1),(-1,0)]#创建方向数组
        res=0#初始化结果
        visited=[[False for i in range(n)]for i in range(m)]#初始化标记数组
        def dfs(grid,visited,x,y):#进行bfs，参数时网格数组，标识数组，当前点的坐标
            queue=[]#初始化队列
            count=1#当前点也算一个，所以初始面积为1
            queue.append((x,y))#将当前点加入到队列中
            visited[x][y]=True#将当前点标记为已遍历
            while queue:#进行遍历
                curx,cury=queue.pop(0)#弹出队头的坐标作为当前坐标
                for dx,dy in dir:#对当前点的四个方向进行遍历
                    nextx,nexty=curx+dx,cury+dy#计算当前点
                    if nextx<0 or nextx>=m or nexty<0 or nexty>=n or visited[nextx][nexty] or grid[nextx][nexty]==0:#如果当前点超过范围或者网格值为0或者已经遍历过，则跳过当前点
                        continue
                    visited[nextx][nexty]=True#将当前点标识为已遍历
                    queue.append((nextx,nexty))#将当前点加入队列中
                    count+=1#面积加一
            return count#返回本岛屿的面积
        for i in range(m):#对格网中每一个点进行遍历
            for j in range(n):
                if not visited[i][j] and grid[i][j]==1:#如果当前点没有被遍历且值为1
                    count=dfs(grid,visited,i,j)#计算当前岛屿的面积
                    res=max(count,res)#重置最大面积
        return res#返回结果
