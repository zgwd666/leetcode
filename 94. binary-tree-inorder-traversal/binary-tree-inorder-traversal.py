#https://leetcode.cn/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
解题思路：采用递归的方式，中序遍历就是左->中->右的次序
'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]#初始化结果列表
        def helper(root):#定义函数用于辅助中序遍历
            if not root:return#当节点为空时返回
            helper(root.left)#先遍历左子树
            res.append(root.val)#遍历当前节点
            helper(root.right)#遍历右子树
        helper(root)#进行遍历
        return res#返回结果
        
