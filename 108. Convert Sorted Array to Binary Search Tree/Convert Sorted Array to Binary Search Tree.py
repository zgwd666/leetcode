#https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
'''
解题思路;对于一个有序的数组，可以取最中间的值作为根节点，其左侧元素均小于它，其右侧元素均大于它，然后对左右数组迭代上述过程就哭呀转换为二叉搜索树
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:return None#判断返回条件，即数组为空
        mid=len(nums)//2#找到数组中间元素作为根节点
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])#遍历左子数组
        root.right=self.sortedArrayToBST(nums[mid+1:])#遍历右子数组
        return root#返回结果
