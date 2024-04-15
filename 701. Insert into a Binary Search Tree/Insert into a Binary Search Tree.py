#https://leetcode.cn/problems/insert-into-a-binary-search-tree/
'''
解题思路：将待插入的值与二叉搜索树的节点值不断对比，大则在右子树找，小则在左子树找，直到遭到叶子节点插入即可
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        valNode=TreeNode(val)#先将值转换为二叉树结点
        if not root:return valNode#如果二叉搜索树为空，则直接返回待插入结点
        if val<root.val:  # 插入的节点值比根节点值小
            if not root.left:#如果左子树不存在
                root.left=valNode#直接插入到左子树
            else:#左子节点存在，就继续在左子节点上找
                self.insertIntoBST(root.left,val)
        if val>root.val : # 插入的节点值比根节点值大
            if not root.right:#如果右子树不存在
                root.right=valNode#直接插入到右子树
            else:#右子节点存在，就继续在右子节点上找
                self.insertIntoBST(root.right,val)
        return root#返回二叉搜索树
