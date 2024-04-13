#https://leetcode.cn/problems/search-in-a-binary-search-tree/
'''
解题思路：采用层序遍历的方式，遍历二叉树的每一个节点，如果该节点的值等于目标值，返回该节点即可，如果完全遍历之后没有找到，则返回None
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
         #第一步，处理特殊情况，如果二叉树为空，直接返回None
        if not root :return None
    	#根节点入队
        queue=[root]
        while queue:#遍历队列
            for _ in range(len(queue)):#遍历二叉树中的每一个节点
                cur=queue.pop(0)#弹出最左侧的节点
                if cur.val==val:#如果节点值等于目标值
                    return cur#返回当前根节点
                if cur.left:#如果当前节点值不等于目标值且存在左子节点
                    queue.append(cur.left)#左子节点入队
                if cur.right:#如果当前节点值不等于目标值且存在右子节点
                    queue.append(cur.right)#右子节点入队
        return None#所有节点遍历完毕但未找到等于目标值的节点，返回None
