#https://leetcode.cn/problems/maximum-depth-of-binary-tree/
'''
解题思路：采用二叉树层序遍历的模板解决的，定义一个count，每遍历一次，count+1，最后返回count即可
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0#判断特殊情况
        queue=[root]#将root放入队列中
        count=0#定义count
        while queue:#遍历列表
            for _ in range(len(queue)):#循环遍历队列中所有节点
                cur=queue.pop(0)#每次从队列头部取出一个节点（queue.pop(0)）
                if cur.left:#如果当前节点有左子节点，将其加入队列
                    queue.append(cur.left)
                if cur.right:#如果当前节点有右子节点，也将其加入队列
                    queue.append(cur.right)
            count+=1#本层遍历完成，count+1
        return count#返回最大深度
