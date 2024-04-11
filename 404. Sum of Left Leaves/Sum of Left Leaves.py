#https://leetcode.cn/problems/sum-of-left-leaves/
'''
解题思路：采用层序遍历的方式，遇到节点时，判断其左子节点是否为叶子节点，如果是就将值加到结果中
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or root.left==None and root.right==None:return 0#判断特殊情况
        result=0#初始化左节点和
        queue=[root]#根节点入队
        while queue:#遍历队列
            for _ in range(len(queue)):#遍历其中每一个节点
                cur=queue.pop(0)#弹出最左侧的节点
                if cur.left:#如果存在左子节点
                    queue.append(cur.left)#将左子节点入队
                    if not cur.left.left and not cur.left.right:#判断左子节点是否为叶子节点，是则将其加到结果中
                        result+=cur.left.val 
                if cur.right:#如果存在右子节点
                    queue.append(cur.right)#将右子节点入队
        return result#返回结果
