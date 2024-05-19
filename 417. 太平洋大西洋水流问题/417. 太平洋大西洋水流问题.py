#https://leetcode.cn/problems/pacific-atlantic-water-flow/
'''
解题思路：
本题的意思就是寻找哪些点可以同时到达太平洋和大西洋。流动的方式只能从高到低流。
其实就是遍历每个点，然后看这个点能不能同时到达太平洋和大西洋。
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)#得到m
        n=len(heights[0])#得到n
        dir=[(0,1),(1,0),(-1,0),(0,-1)]#创建方向数组
        visited=[[[False for i in range(2)]for i in range(n)]for i in range(m)]#创建标识数组
        def dfs(heights,visited,queue):#BFS函数，传入的参数包括网格数组，包含四周为陆地点的坐标的队列，标识数组
            while queue:#进行遍历
                curx,cury,cursign=queue.pop(0)#弹出队头的坐标作为当前坐标
                for dx,dy in dir:#对当前点的四个方向进行遍历
                    nextx,nexty=curx+dx,cury+dy#计算当前点
                    if nextx<0 or nextx>=m or nexty<0 or nexty>=n:#超出边界，跳过
                        continue
                    if heights[nextx][nexty]<heights[curx][cury] or visited[nextx][nexty][cursign]:#当前点被遍历过或者当前点的高度低于前一个点的高度，也跳过
                        continue
                    visited[nextx][nexty][cursign]=True#将当前点进行标记
                    queue.append((nextx,nexty,cursign))#将当前点加入到队列中
        res=[]#初始化结果数组
        queue=[]#初始化队列
        for i in range(m):#对左右边界上的点进行遍历，左边界的点可以进入太平洋，则0为True，右边界的点可以进入大西洋，则1为True，将点加入队列
            visited[i][0][0]=True
            visited[i][n-1][1]=True
            queue.append((i,0,0))
            queue.append((i,n-1,1))
        for i in range(n):#对上下边界上的点进行遍历，上边界的点可以进入太平洋，则0为True，下边界的点可以进入大西洋，则1为True，将点加入队列
            visited[0][i][0]=True
            visited[m-1][i][1]=True
            queue.append((0,i,0))
            queue.append((m-1,i,1))
        dfs(heights,visited,queue)#从边界点向内进行遍历，对大西洋和太平洋能到的点进行标记
        for i in range(m):#对每一个点进行遍历
            for j in range(n):
                if visited[i][j][0] and visited[i][j][1]:#如果当前点既能到达大西洋又能到达太平洋，则将该点加入结果中
                    res.append([i,j])
        return res#返回结果
