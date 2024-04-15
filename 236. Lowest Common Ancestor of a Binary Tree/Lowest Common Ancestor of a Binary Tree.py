#https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
'''
解题思路：考虑通过递归对二叉树进行先序遍历，当遇到节点 ppp 或 qqq 时返回。从底至顶回溯，当节点 p,qp, qp,q 在节点 rootrootroot 的异侧时，节点 rootrootroot 即为最近公共祖先，则向上返回 root
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #第一步，基本情况：如果当前的根节点root为空，或者root就是p或q之一，那么这个节点就是我们要找的最低公共祖先。这是因为在递归过程中，一旦我们到达了目标节点之一，就没有必要继续向上搜索了。
        if not root or root==p or root==q:
            return root
        #第二步，递归搜索：在root不为空且root既不是p也不是q的情况下，我们分别在root的左子树和右子树中递归地搜索p和q。我们通过left = self.lowestCommonAncestor(root.left, p, q)和right = self.lowestCommonAncestor(root.right, p, q)来实现这一点。
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        #第三步，合并结果：
        '''
        在递归返回后，我们有四种可能的情况：
        如果在左子树中找到了p和q的最低公共祖先（即left不为空），而在右子树中没有找到（即right为空），那么我们返回left。
        如果在右子树中找到了p和q的最低公共祖先（即right不为空），而在左子树中没有找到（即left为空），那么我们返回right。
        如果left和right都不为空，这意味着p和q分别位于root的左右两侧，因此root就是它们的最低公共祖先。
        如果left和right都为空，这意味着在当前子树中没有找到p或q，因此我们可以继续向上返回，直到找到它们或者到达空节点。
        '''
        if not left:return right
        if not right:return left
        return root
