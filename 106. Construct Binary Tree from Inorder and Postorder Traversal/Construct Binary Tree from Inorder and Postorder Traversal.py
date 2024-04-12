#https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
'''
解题思路：如何根据两个顺序构造一个唯一的二叉树，就是以后序遍历的最后一个元素为切割点，先切中序数组，根据中序数组反过来再切后序数组，一层一层切下去，每次后序数组的最后一个元素就是节点元素。

代码的逻辑就是：

1. 第一步，如果数组的大小为0，说明是空节点了
2. 第二步，如果数组不为空，则取出后序数组的最后一个元素作为节点元素
3. 第三步，找到后续数组最后一个元素在中序数组中的位置，作为切割点
4. 第四步，切割中序数组，切成中序左数组和中序右数组
5. 第五步，切割后序数组，切成后序左数组和后序右数组
6. 递归处理左区间和右区间
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:return None # 第一步: 特殊情况讨论: 树为空. (递归终止条件)
        val=postorder[-1]  # 第二步: 后序遍历的最后一个就是当前的中间节点.
        root=TreeNode(val)
        index=inorder.index(val) # 第三步: 找切割点.
        # 第四步: 切割inorder数组. 得到inorder数组的左,右半边.
        left_inorder=inorder[:index]
        right_inorder=inorder[index+1:]
        # 第五步: 切割postorder数组. 得到postorder数组的左,右半边.
          # ⭐️ 重点1: 中序数组大小一定跟后序数组大小是相同的.
        left_postorder=postorder[:len(left_inorder)]
        right_postorder=postorder[len(left_inorder):-1]
        # 第六步: 递归
        root.left=self.buildTree(left_inorder,left_postorder)
        root.right=self.buildTree(right_inorder,right_postorder)
        # 第七步: 返回答案
        return root
