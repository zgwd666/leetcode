#https://leetcode.cn/problems/binary-tree-right-side-view/
'''
解题思路：采用层序遍历的方式，依次遍历每一层，将每一层最右边也就是当层数组中的最右侧的元素放入result数组中，随后返回result就可以
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []#判断特殊情况
        queue=[root]#将root放入队列中
        result=[]#初始化结果列表
        while queue:#遍历列表
            level=[]#初始化当层节点值
            for _ in range(len(queue)):#遍历本层的节点
                cur=queue.pop(0)#弹出节点，从左边弹出
                level.append(cur.val)#先添加左节点
                if cur.left:
                    queue.append(cur.left)
                if cur.right:#再添加右节点
                    queue.append(cur.right)
            result.append(level[-1])#添加本层最右侧的节点值
        return result#返回反转后结果
