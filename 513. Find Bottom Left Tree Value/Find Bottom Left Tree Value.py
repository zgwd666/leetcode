#https://leetcode.cn/problems/find-bottom-left-tree-value/
'''
解题思路：找树左下角的值就是寻找二叉树最深的一层中最靠左的节点值。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:return root#判断特殊情况
        queue=[root]#根节点入队
        while queue:#遍历队列
            level=[]#初始化列表
            for _ in range(len(queue)):#遍历其中每一个节点
                cur=queue.pop(0)#弹出最左侧的节点
                level.append(cur.val)#添加当前节点值
                if cur.left:#如果存在左子节点
                    queue.append(cur.left)#将左子节点入队
                if cur.right:#如果存在右子节点
                    queue.append(cur.right)#将右子节点入队
        return level[0]#返回最后一层的最左侧值
