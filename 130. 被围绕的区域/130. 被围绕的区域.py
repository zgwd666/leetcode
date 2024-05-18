#https://leetcode.cn/problems/surrounded-regions/
'''
解题思路：本题采用BFS的思路，通过先将与四周相连的O进行标记，然后将没有与边界连通的O也就是被X包围的O改为X
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)#得到m
        n=len(board[0])#得到n
        visited=[[False for i in range(n)]for i in range(m)]#初始化标记数组
        queue=[]#初始化队列
        dir=[(0,1),(1,0),(0,-1),(-1,0)]#创建方向数组
        def bfs(board,visited,queue):#BFS函数，传入的参数包括网格数组，包含四周为陆地点的坐标的队列，标识数组
            while queue:#进行遍历
                curx,cury=queue.pop(0)#弹出队头的坐标作为当前坐标
                for dx,dy in dir:#对当前点的四个方向进行遍历
                    nextx,nexty=curx+dx,cury+dy#计算当前点
                    if nextx<0 or nextx>=m or nexty<0 or nexty>=n or visited[nextx][nexty] or board[nextx][nexty]=='X':#如果当前点超过范围或者网格值为X或者已经遍历过，则跳过当前点
                        continue
                    visited[nextx][nexty]=True#将当前点标识为已遍历
                    queue.append((nextx,nexty))#将当前点加入队列中
        for i in range(m):
            if board[i][0]=='O':#将左边界和右边界的O标识为已遍历且将坐标加入队列
                visited[i][0]=True
                queue.append((i,0))
            if board[i][n-1]=='O':
                visited[i][n-1]=True
                queue.append((i,n-1))
        for i in range(n):#将上边界和下边界的O标识为已遍历且将坐标加入队列
            if board[0][i]=='O':
                visited[0][i]=True
                queue.append((0,i))
            if board[m-1][i]=='O':
                visited[m-1][i]=True
                queue.append((m-1,i))
        bfs(board,visited,queue)#对与四周边界相连的O都进行标识
        for i in range(m):#进行遍历，将非四周相连的0转换为X
            for j in range(n):
                if board[i][j]=='O' and not visited[i][j]:
                    board[i][j]='X'
