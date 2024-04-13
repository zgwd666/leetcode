#https://leetcode.cn/problems/merge-two-binary-trees/
'''
解题思路：题目的意思可以简单理解为将两个树相加，其中Null可以视为相加中的0，那么就可以新建一个二叉树根节点，其值等于第一棵树根节点值加上第二棵树跟节点值，之后每棵树都是如此相加，直到遇到都是Null为止。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #第一步，判断返回条件，可以简单理解为返回不为None的节点
        if not root2:return root1
        if not root1 :return root2
    	#第二步，新建树的跟节点值为两颗树跟节点值相加
        root=TreeNode(root1.val+root2.val)
        #第三步，递归处理左子树和右子树
        root.left=self.mergeTrees(root1.left,root2.left)
        root.right=self.mergeTrees(root1.right,root2.right)
        #第四步: 返回答案
        return root
