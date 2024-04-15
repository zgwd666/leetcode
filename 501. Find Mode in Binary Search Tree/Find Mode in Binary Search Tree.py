#https://leetcode.cn/problems/find-mode-in-binary-search-tree/
'''
解题思路:采用哈希表的方式，将二叉进行遍历，遍历中的节点值与出现的次数存储在哈希表中，然后遍历哈希表，找出众数即可。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dict1={}#初始化哈希表
        queue=[root]#根节点入队
        while queue:#遍历队列
            for _ in range(len(queue)):#遍历队列每一个元素
                cur=queue.pop(0)#弹出队列最左侧的节点
                if cur.val not in dict1:#将值与对应的频率存放在哈希表中
                    dict1[cur.val]=1
                else:
                    dict1[cur.val]+=1
                if cur.left:#存在左节点，左节点入队
                    queue.append(cur.left)
                if cur.right:#存在右节点，右节点入队
                    queue.append(cur.right)
        result=[]#初始化结果列表
        for key ,value in dict1.items():#遍历哈希表
            if result==[]:#如果结果列表为空，也就是遍历第一个元素
                result.append(key)#先将第一个元素的key添加到结果列表中
                count=value#更新频率
                continue#跳转到第二个值
            if value==count:#从第二个元素往后，如果频率相等，则都加入结果列表中
                result.append(key)
            if value>count:#如果频率比之前的大
                result=[key]#则将之前结果列表中的元素全部剔除，添加上该频率对应的key
                count=value#更新频率
        return result#返回结果列表
