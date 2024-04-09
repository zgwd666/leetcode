#https://leetcode.cn/problems/subtree-of-another-tree/
'''
解题思路;判断节点值是否一致或者是否与该结点的左右某节点一致
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:return True#二者均为空，则肯定为子树
        if not root or not subRoot:return False#二者仅有一者为空，则必不为子树
        return self.isSameTree(root,subRoot) or self.isSubtree(root.left,subRoot)or self.isSubtree(root.right,subRoot)#进行递归，条件是是否与当前节点完全一致或者与当前节点的左右某一子树完全一致
    def isSameTree(self,root,subRoot):#判断两棵树是否完全一致
        if not root and not subRoot:return True#二者均为空，则肯定一致
        if not root or not subRoot:return False#二者仅有一者为空，则必不一致
        return root.val==subRoot.val and self.isSameTree(root.left ,subRoot.left) and self.isSameTree(root.right,subRoot.right)#两棵树完全一致的要求是节点值一致且左右子树完全一致
