#https://leetcode.cn/problems/maximum-depth-of-n-ary-tree/
'''
解题思路：采用层序遍历的思路，跟二叉树的最大深度一样，就是将二叉树的左右子树变为children
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:return 0#判断特殊情况
        queue=[root]#根节点入队
        count=0#初始化深度
        while queue:#遍历队列
            for _ in range(len(queue)):#遍历队列中每一个节点
                cur=queue.pop(0)#弹出队列中最先进队的节点
                for i in cur.children:#遍历cur的每一个子节点，将其入队
                    queue.append(i)
            count+=1#深度加1
        return count#返回深度
