#https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''
解题思路：如何根据两个顺序构造一个唯一的二叉树，就是以前序遍历的第一个元素为切割点，先切中序数组，根据中序数组反过来再切前序数组，一层一层切下去，每次前序数组的第一个元素就是节点元素。

代码的逻辑就是：

1. 第一步，如果数组的大小为0，说明是空节点了
2. 第二步，如果数组不为空，则取出前序数组的第一个元素作为节点元素
3. 第三步，找到前序数组第一个元素在中序数组中的位置，作为切割点
4. 第四步，切割中序数组，切成中序左数组和中序右数组
5. 第五步，切割q前序数组，切成前序左数组和前序右数组
6. 递归处理左区间和右区间
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 第一步: 特殊情况讨论: 树为空. 或者说是递归终止条件
        if not preorder:return None
        # 第二步: 前序遍历的第一个就是当前的中间节点.
        val=preorder[0]
        root=TreeNode(val)
         # 第三步: 找切割点.
        index=inorder.index(val)
           # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        left_inorder=inorder[:index]
        right_inorder=inorder[index+1:]
        # 第五步: 切割preorder数组. 得到preorder数组的左,右半边.
        # ⭐️ 重点1: 中序数组大小一定跟前序数组大小是相同的.
        left_preorder=preorder[1:len(left_inorder)+1]
        right_preorder=preorder[len(left_inorder)+1:]
        # 第六步: 递归
        root.left=self.buildTree(left_preorder,left_inorder)
        root.right=self.buildTree(right_preorder,right_inorder)
        # 第七步: 返回答案
        return root
