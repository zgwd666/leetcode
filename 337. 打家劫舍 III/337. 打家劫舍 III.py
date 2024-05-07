#https://leetcode.cn/problems/house-robber-iii/
'''
解题思路：将问题转换为对当前节点的选与不选的问题。
选当前节点时，以当前节点为根的子树最大点权和
不选当前节点时，以当前节点为根的子树最大点权和
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def traversal(root):#进行遍历
            if not root:#当不存在根节点的时候，返回0
                return(0,0)
            l_rob,l_not_rob=traversal(root.left)#返回左子节点选与不选的值
            r_rob,r_not_rob=traversal(root.right)#返回右子节点选与不选的值
            val_rob=l_not_rob+r_not_rob+root.val#选当前节点，那么值等于当前节点值+左子节点不选+右子节点不选的值
            val_not_rob=max(l_rob,l_not_rob)+max(r_rob,r_not_rob)#不限当前节点，那么值就是选选左子节点和不选左子节点的最大值+选右子节点和不选右子节点的做大致
            return val_rob,val_not_rob#返回选当前节点，不选当前节点的最大值
        return max(traversal(root))#返回最大值
