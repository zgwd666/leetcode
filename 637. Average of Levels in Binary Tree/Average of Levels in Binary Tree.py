#https://leetcode.cn/problems/average-of-levels-in-binary-tree/
'''
解题思路：采用层序遍历的方式，依次遍历每一层，将每一层求一个总和，然后记录本层的节点个数，最后将sum/count放入result之中，随后返回result就可以。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:return []#判断特殊情况
        result=[]#初始化结果列表
        queue=[root]#将root放入队列中
        while queue:#遍历列表
            sumLevel=0#初始化本层的节点和
            count=0#初始化本层的节点数量
            for _ in range(len(queue)):#遍历本层的节点
                cur=queue.pop(0)#弹出节点，从左边弹出
                sumLevel+=cur.val#求本层节点和
                count+=1#记录本层的节点数量
                if cur.left:#先添加左节点
                    queue.append(cur.left)
                if cur.right:#再添加右节点
                    queue.append(cur.right)
            result.append(sumLevel/count)#添加本层节点和平均值
        return result#返回结果
