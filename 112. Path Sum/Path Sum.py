#https://leetcode.cn/problems/path-sum/
'''
解题思路：本题需要计算从根节点到叶子节点的所有路径中，每个节点值的总和是否等于target，存在则返回True，否则返回False。那么我们就可以层序遍历二叉树，遇到叶子节点就将该路径上的所有的值加起来，然后与目标值进行对比，如果相等，返回True，遍历完成无匹配值则返回False
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:return False#判断特殊情况
        queue=[root]#将根节点入队
        path_queue=[root.val]#将根节点的值入路径队
        while queue:#遍历队列
            for _ in range(len(queue)):#遍历其中每一个节点
                cur=queue.pop(0)#弹出最左侧的节点
                path_cur=path_queue.pop(0)#弹出与其对应的路径
                if cur.left:#如果存在左子节点
                    queue.append(cur.left)#将左子节点入队
                    path_queue.append(path_cur+cur.left.val)#将本条路径的前缀和入路径队
                if cur.right:#如果存在右子节点
                    queue.append(cur.right)#将右子节点入队
                    path_queue.append(path_cur+cur.right.val)#将本条路径的前缀和入路径队
                if not cur.left and not cur.right:#遇到叶子节点
                    if path_cur==targetSum:return True#判断是否与目标值相等
        return False
