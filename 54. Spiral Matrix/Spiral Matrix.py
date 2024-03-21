#https://leetcode.cn/problems/spiral-matrix/
'''
解题思路：本题还是模拟矩阵的思路
按照从左到右、从上到下、从右到左从下到上的顺寻进行遍历
结束条件是左大于右 或者上大于下
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]#定义结果空数组
        l,r,t,b=0,len(matrix[0])-1,0,len(matrix)-1#定义边界初始值，分别为0，n-1，0，m-1
        while True:#遍历
            for i in range(l,r+1):#从左到右，左闭右闭
                res.append(matrix[t][i])#添加元素
            t+=1#行下移
            if t>b:break#当上大于下跳出循环
            for i in range(t,b+1):#从上到下，左闭右闭
                res.append(matrix[i][r])#添加元素
            r-=1#列左移
            if r<l:break#当左大于右跳出循环
            for i in range(r,l-1,-1):#从右到左，左闭右闭
                res.append(matrix[b][i])#添加元素
            b-=1#行上移
            if b<t:break#当上大于下跳出循环
            for i in range(b,t-1,-1):#从下到上，左闭右闭
                res.append(matrix[i][l])#添加元素
            l+=1#列右移
            if l>r:break#当左大于右跳出循环
        return res #返回结果
