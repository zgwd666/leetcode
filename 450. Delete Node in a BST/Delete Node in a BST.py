# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 如果根节点为空，则直接返回None
        if not root:return root
    	# 如果要删除的键值key大于根节点的值，递归地在右子树中查找和删除
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        # 如果要删除的键值key小于根节点的值，递归地在左子树中查找和删除
        elif root.val>key:
            root.left=self.deleteNode(root.left,key)
        else:
            # 找到了要删除的节点，分为两种情况处理
            # 如果要删除的节点没有左子节点或没有右子节点
            if not root.left or not root.right:
                 # 如果有左子节点，则返回左子节点，否则返回右子节点
                root=root.left if root.left else root.right
            else:
                 # 如果要删除的节点有两个子节点，找到右子树的最小节点（后继节点）
                node=root.left
                # 遍历到左子树的最右节点，即后继节点
                while node.right:
                    node=node.right
                # 将要删除的节点的值替换为后继节点的值
                node.left=self.deleteNode(root.left,node.val)
                node.right=root.right
                root=node
        # 返回更新后的根节点
        return root
