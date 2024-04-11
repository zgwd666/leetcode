#https://leetcode.cn/problems/balanced-binary-tree/
'''
解题思路：采用迭代的方法，对于每个节点来说，它自己的左右子节点的高差不超过1，且它的左右子结点的左右子节点的高差也不超过1.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:return True#确定终止条件
        def height(node):#定义辅助函数用于计算该点的深度
            if not node:return 0#确定终止条件
            return 1+max(height(node.left),height(node.right))#计算深度
        return abs(height(root.right)-height(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)#不断迭代，所有的节点都满足条件才返回True
