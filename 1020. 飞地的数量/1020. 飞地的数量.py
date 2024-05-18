#https://leetcode.cn/problems/number-of-enclaves/
'''
解题思路：
本题要求找到不靠边的陆地面积，那么我们只要从周边摘到陆地然后通过dfs或者bfs将周边靠陆地且相邻的陆地都变成海洋，然后再去重新遍历地图时，统计此时还剩下的陆地就可以了。
'''
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)#得到m
        n=len(grid[0])#得到n
        dir=[(0,1),(1,0),(0,-1),(-1,0)]#创建方向数组
        visited=[[False for i in range(n)]for i in range(m)]#初始化标记数组
        queue=[]#初始化队列
        def dfs(grid,queue,visited):#BFS函数，传入的参数包括网格数组，包含四周为陆地点的坐标的队列，标识数组
            while queue:#进行遍历
                curx,cury=queue.pop(0)#弹出队头的坐标作为当前坐标
                for dx,dy in dir:#对当前点的四个方向进行遍历
                    nextx,nexty=curx+dx,cury+dy#计算当前点
                    if nextx<0 or nextx>=m or nexty<0 or nexty>=n or visited[nextx][nexty] or grid[nextx][nexty]==0:#如果当前点超过范围或者网格值为0或者已经遍历过，则跳过当前点
                        continue
                    visited[nextx][nexty]=True#将当前点标识为已遍历
                    queue.append((nextx,nexty))#将当前点加入队列中
        res=0#初始化结果
        for i in range(m):#将左边界和右边界的陆地标识为已遍历且将坐标加入队列
            if grid[i][0]==1:
                visited[i][0]=True
                queue.append((i,0))
            if grid[i][n-1]==1:
                visited[i][n-1]=True
                queue.append((i,n-1))
        for i in range(n):#将上边界和下边界的陆地标识为已遍历且将坐标加入队列
            if grid[0][i]==1:
                visited[0][i]=True
                queue.append((0,i))
            if grid[m-1][i]==1:
                visited[m-1][i]=True
                queue.append((m-1,i))
        dfs(grid,queue,visited)#对与四周边界相连的陆地都进行标识
        for i in range(m):#进行遍历，将非四周相连的陆地的陆地进行统计
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    res+=1
        return res#返回结果
