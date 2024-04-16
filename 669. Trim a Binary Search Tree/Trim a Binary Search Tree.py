#https://leetcode.cn/problems/trim-a-binary-search-tree/
'''
解题思路：
对于二叉树的递归，只需要清楚当前的root需要干什么即可
分三种情况：
1. 当root.val<L时候，只需要递归右子树（root发生改变）
2. 当root.val>R时候，只需要递归左子树（root发生改变）
3. root.val在L和R之间，同时递归左右子树（root没有发生改变）
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:return root#当遍历到空节点发，安徽
        if root.val<low:#当root.val<L时候，只需要递归右子树（root发生改变）
            root=self.trimBST(root.right,low,high)
        elif root.val>high:#当root.val>R时候，只需要递归左子树（root发生改变）
            root=self.trimBST(root.left,low,high)
        else:#root.val在L和R之间，同时递归左右子树（root没有发生改变）
            root.left=self.trimBST(root.left,low,high)
            root.right=self.trimBST(root.right,low,high)
        return root#返回结果
