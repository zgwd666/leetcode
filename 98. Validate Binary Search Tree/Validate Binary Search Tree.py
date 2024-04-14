#https://leetcode.cn/problems/validate-binary-search-tree/
'''
解题思路：验证是否为二叉搜索树，就是判断根节点的左右节点是否满足田间，然后迭代判断其子节点的子结点是否在范围内
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,minValue,maxValue):#定义辅助函数，需要传入的参数为当前节点，最大值，最小值
            if not root:return True#当前节点为空，满足二叉搜索树的定义，返回True
            if not (minValue<root.val<maxValue):#如果当前节点的值不在范围内，返回False
                return False
            return helper(root.left,minValue,root.val) and helper(root.right,root.val,maxValue)#迭代当前节点的子结点，对于左节点，其最小值范围不变，最大值为当前节点的值；对于右节点，其最大值范围不变，最小值为当前节点的值
        return helper(root,float('-inf'),float('inf'))#进行迭代判断
