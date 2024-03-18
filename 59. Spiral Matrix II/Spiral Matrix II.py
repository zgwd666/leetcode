#https://leetcode.cn/problems/spiral-matrix-ii/
'''
本题是一个模拟矩阵，主要是抓住边界条件
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums=[[0 for _ in range(n)]for _ in range(n)]#先初始化一个数组
        l,r,t,b=0,n-1,0,n-1#定义边界，左上边界为（0，0），右上边界为（0，n-1），右下边界为（n-1，n-1），左下边界为（n-1，0）
        num,target=1,n*n#定义开始数字和结束的数字
        while num<=target:#当当前数字不大于结尾数字时，执行遍历
            for i in range(l,r+1):#首先是从左到右遍历，
                nums[t][i]=num#此时赋值，行不变，列变化
                num+=1#数字加一
            t+=1#遍历结束，转到下一行
            for i in range(t,b+1):#执行从上到下的遍历
                nums[i][r]=num#此时赋值。列不变，行变化
                num+=1#数字加一
            r-=1#遍历结束，转到左边一列
            for i in range(r,l-1,-1):#执行从右到左的遍历
                nums[b][i]=num#此时赋值，行不变，列变化
                num+=1#数字加一
            b-=1#转到上一行
            for i in range(b,t-1,-1):#执行从上到下的遍历
                nums[i][l]=num此时赋值，列不变，行变化
                num+=1#数字加一
            l+=1#遍历结束，转到右边一列
        return nums#返回结果数组
