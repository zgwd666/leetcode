#https://leetcode.cn/problems/n-ary-tree-level-order-traversal/
'''
解题思路：本题与层序遍历的思路基本一致，需要注意的是一层可能有多个节点，也就是children是一个链表节点的列表而不是单个的链表节点，需要将链表节点从其中的列表中遍历出来存入队列中。
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []#判断特殊情况
        result=[]#初始化结果列表
        queue=[root]#将root放入队列中
        while queue:#遍历列表
            level=[]#初始化当层节点值
            for _ in range(len(queue)):#遍历本层的节点
                cur=queue.pop(0)#弹出节点，从左边弹出
                level.append(cur.val)#记录当前节点的值
                for children in cur.children:#将下一层的链表节点一一遍历出来
                    queue.append(children)
            result.append(level)#添加结果
       return result#返回结果
