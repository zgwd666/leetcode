#https://leetcode.cn/problems/minimum-depth-of-binary-tree/
'''
解题思路：在层序遍历的时候需要叶子节点就跳出遍历，返回深度即可。
叶子结点的特点是左子节点和右子节点都为空
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0#判断特殊情况
        queue=[root]#将root放入队列中
        count=0#定义count
        flag=1#定义指示器，用于指示是否遍历到叶子节点
        while queue and flag:#循环遍历队列 当遍历完或者遍历到叶子节点即跳出
            for _ in range(len(queue)):#循环遍历队列中所有节点
                cur=queue.pop(0)#每次从队列头部取出一个节点（queue.pop(0)）
                if not cur.left and not cur.right:#当左子节点和右子节点都为空的时候，就是遍历到叶子节点，将指示器设置为0
                    flag=0
                if cur.left:#如果当前节点有左子节点，将其加入队列
                    queue.append(cur.left)
                if cur.right:#如果当前节点有右子节点，也将其加入队列
                    queue.append(cur.right)
            count+=1#本层遍历完成，count+1
        return count#返回最大深度
