#https://leetcode.cn/problems/symmetric-tree/
'''
解题思路：采用层序遍历的思路，此时在进行遍历中将每一个子树无论存在与否都存入队列中，然后在下一层遍历时，需要判断是否存在节点
每层遍历的时候需要记录下每个节点，不存在的节点用None占位，最后对比原数组和反转数组是否一致
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:return False#判断特殊情况
        queue=[root]#将root放入队列中
        while queue:#遍历列表
            level=[]#初始化当层节点值
            for _ in range(len(queue)):#循环遍历队列中所有节点
                cur=queue.pop(0)#每次从队列头部取出一个节点（queue.pop(0)）
                if cur:#判断当前节点是否为空
                    level.append(cur.val)#将节点存入当层数组
                    queue.append(cur.left)#添加左子节点，无论节点是否为None
                    queue.append(cur.right)#添加右子节点，无论节点是否为None
                else:
                    level.append(None)#节点为空，用None占位
            if level!=level[::-1]:return False#判断数组和反转数组是否一致，不一致就不是对称     
        return True#所有的错误情况排除，那就是对称
