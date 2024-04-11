#https://leetcode.cn/problems/binary-tree-paths/
'''
解题思路：定义两个队列，一个队列用来存储节点，另一个队列用来存储该节点所对应的路径。然后正常层序遍历，遇到叶子节点（也就是左右子节点均为空的节点），将路径加入到结果中即可。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:return []#判断特殊情况
        result=[]#初始化结果列表
        queue=[root]#将根节点入队
        path_queue=[str(root.val)]#将根节点的值入路径对
        while queue:#遍历队列
            for _ in range(len(queue)):#遍历其中每一个节点
                cur=queue.pop(0)#弹出最左侧的节点
                path=path_queue.pop(0)#弹出与其队列的路径
                if cur.left:#如果存在左子节点
                    queue.append(cur.left)#将左子节点入队
                    path_queue.append(path+'->'+str(cur.left.val))#将路径+左子节点的值入路径队
                if cur.right:#如果存在右子节点
                    queue.append(cur.right)#将右子节点入队
                    path_queue.append(path+'->'+str(cur.right.val))#将路径+右子节点的值入路径队
                if not cur.left and not cur.right:#如果遍历到叶子节点
                    result.append(path)#将其对应的路径加入到结果列表中
        return result#返回结果列表
