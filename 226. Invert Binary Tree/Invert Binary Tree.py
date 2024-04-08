#https://leetcode.cn/problems/invert-binary-tree/
'''
解题思路：采用广度优先遍历（层序遍历）的思路，在正常遍历的同时，将每一层的左右节点进行交换即可
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:return root#判断特殊情况
        queue=[root]#将root放入队列中
        while queue:#遍历列表
            for _ in range(len(queue)):#循环遍历队列中所有节点
                cur=queue.pop(0)#每次从队列头部取出一个节点（queue.pop(0)）
                if cur.left and cur.right:#如果左右子结点都存在，进行交换，且将交换后的左右子节点放入队列中
                    temp=cur.left
                    cur.left=cur.right
                    cur.right=temp
                    queue.append(cur.left)
                    queue.append(cur.right)
                elif cur.left:#如果只存在左节点，就将左节点赋值为右节点，左节点指向None，将新的右节点存入队列中
                    cur.right=cur.left
                    cur.left=None
                    queue.append(cur.right)
                elif cur.right:#如果只存在右节点，就将右节点赋值为左节点，右节点指向None，将新的左节点存入队列中
                    cur.left=cur.right
                    cur.right=None
                    queue.append(cur.left)
        return root#返回root
