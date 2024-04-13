#https://leetcode.cn/problems/maximum-binary-tree/
'''
解题思路：如何根据数组构建最大二叉树，就是一个不断选取数组中最大值，然后根据最大值将数组分割为左右两个部分，对左右两个部分分别重复以上的步骤

代码的逻辑就是：

1. 第一步，如果数组的大小为0，说明是空节点
2. 第二步，如果数组不为空，则取出数组中最大的元素作为根节点
3. 第三步，找到最大节点的索引作为切分点
4. 第四步，切割数组，切成左数组和组
5. 递归处理左区间和右区间
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 第一步: 特殊情况讨论: 树为空. 或者说是递归终止条件
        if not nums:return None
    	# 第二步: 数组中的最大值就是当前的中间节点.
        maxValue=max(nums)
        root=TreeNode(maxValue)
        # 第三步: 找切割点.
        index=nums.index(maxValue)
        #第四步，切割数组，切成左数组和组
        leftNums=nums[:index]
        rightNums=nums[index+1:]
        #第五步，递归处理左区间和右区间
        root.left=self.constructMaximumBinaryTree(leftNums)
        root.right=self.constructMaximumBinaryTree(rightNums)
         # 第六步: 返回答案
        return root
