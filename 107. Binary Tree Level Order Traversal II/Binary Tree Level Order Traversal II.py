#https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
'''
解题思路：和层序遍历一样，最后反转结果输出即可
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []#判断特殊情况
        result=[]#初始化结果列表
        queue=[root]#将root放入队列中
        while queue:#遍历列表
            level=[]#初始化当层节点值
            for _ in range(len(queue)):#遍历本层的节点
                cur=queue.pop(0)#弹出节点，从左边弹出
                level.append(cur.val)#记录节点值
                if cur.left:#先添加左节点
                    queue.append(cur.left)
                if cur.right:#再添加右节点
                    queue.append(cur.right)
            result.append(level)#添加本层节点数值
        return result[::-1]#返回反转后结果
