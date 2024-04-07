#https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
'''
解题思路：采用层序遍历的方式，依次遍历每一层，将每一层求当层的最大值，并将其放入result之中，随后返回result就可以。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []#判断特殊情况
        result=[]#初始化结果列表
        queue=[root]#将root放入队列中
        while queue:#遍历列表
            maxLevle=queue[0].val#初始化本层的最大值为最左边节点的值
            for _ in range(len(queue)):#遍历本层的节点
                cur=queue.pop(0)#弹出节点，从左边弹出
                if cur.val>maxLevle:#对比计算最大值
                    maxLevle=cur.val
                if cur.left:#先添加左节点
                    queue.append(cur.left)
                if cur.right:#再添加右节点
                    queue.append(cur.right)
            result.append(maxLevle)#记录本层最大值
        return result#返回结果
