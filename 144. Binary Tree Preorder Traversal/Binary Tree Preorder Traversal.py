#https://leetcode.cn/problems/binary-tree-preorder-traversal/
'''
解题思路：采用递归的思路，确定三要素：
1.传入参数：传入当前的结点 返回为空 因为在递归之中已经添加到res中
2.终止条件：当前的结点为空就返回
3.单层逻辑：对于一个结点，前序遍历总是按照自身-左子节点-右子节点的顺序进行遍历
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]#初始化结果列表
        def dfs(root):#定义递归函数，传入当前结点作为参数
            if not root:return []#确定递归终止条件，即当前结点为空，就返回
            res.append(root.val)#结果列表添加当前节点的值
            dfs(root.left)#遍历其左子节点
            dfs(root.right)#遍历其右子节点
        dfs(root)#调用递归函数
        return res#返回结果列表
