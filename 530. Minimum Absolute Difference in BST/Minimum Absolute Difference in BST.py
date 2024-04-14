#https://leetcode.cn/problems/minimum-absolute-difference-in-bst/
'''
解题思路:因为题目中的意思是任意节点直接的差值，那就可以通过层序遍历的方式将二叉树中的所有节点的值遍历出来，在采用一个双重遍历，求出最小值
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        temp=[]#初始化值数组
        queue=[root]#根节点入队
        while queue:#遍历队列
            for _ in range(len(queue)):#遍历队列中每一个节点
                cur=queue.pop(0)#弹出队列最左侧的节点
                temp.append(cur.val)#将点的值加入之数组
                if cur.left:#存在左节点，左节点入队
                    queue.append(cur.left)
                if cur.right:#存在右节点，右节点入队
                    queue.append(cur.right)
        minValue=abs(temp[0]-temp[1])#初始化最小值
        for i in range(0,len(temp)):#双重遍历求最小值
            for j in range(i+1,len(temp)):
                if abs(temp[i]-temp[j])<minValue:
                    minValue=abs(temp[i]-temp[j])
        return minValue#返回最小值
