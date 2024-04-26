#https://leetcode.cn/problems/candy/
'''
解题思路：
规则定义：设学生A和学生B左右相邻，A在B的左边：

- 左边规则：如果ratingsB>ratingsA:B的糖比A的糖数量多
- 右边规则：如果ratingsA>ratingsB:A的糖比B的糖数量多

相邻的学生中，评分高的学生必须获得更多的糖果等价于所有的学生满足做过则且满足右规则。
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings)==1:return 1#判断特殊情况
        left=[1]*len(ratings)#初始化左数组
        right=[1]*len(ratings)#初始化右数组
        for i in range(1,len(ratings)):#从左向右遍历
            if ratings[i]>ratings[i-1]:#如果右边的比左边的大
                left[i]=left[i-1]+1#则右边的糖果比左边的加1
        for i in range(len(ratings)-1,0,-1):#从左向右遍历
            if ratings[i]<ratings[i-1]:#如果右边的比左边的小
                right[i-1]=right[i]+1#则左边的糖果比左边的加1
        for i in range(len(ratings)):#对左右两个数组进行遍历，找出每个位置应给予的糖果等于左边和右边中的最大值
            left[i]=max(left[i],right[i])
        return sum(left)#返回糖果和
        
