#https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
'''
解题思路：本题依然是层序遍历，只不过在单层遍历的时候记录一下本层的头部节点，然后在遍历的时候让前一个节点指向本节点就可以了
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:return root#判断特殊情况
        queue=[root]#将root放入队列中
        while queue:#遍历列表
            prev=None初始化一个变量prev，用于保存当前层的前一个节点
            for _ in range(len(queue)):循环遍历队列中所有节点
                node=queue.pop(0)每次从队列头部取出一个节点（queue.pop(0)）
                if prev:如果prev不为空，说明当前节点不是这一层的第一个节点，因此需要将前一个节点的next指针指向当前节点，完成连接
                    prev.next=node
                prev=node更新prev为当前节点，为下一次循环做准备
                if node.left:如果当前节点有左子节点，将其加入队列
                    queue.append(node.left)
                if node.right:如果当前节点有右子节点，也将其加入队列
                    queue.append(node.right)
        return root循环结束后，返回根节点root
