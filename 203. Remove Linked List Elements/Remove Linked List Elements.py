#https://leetcode.cn/problems/remove-linked-list-elements/
'''
解题思路：
本题是链表删除操作，采用定义虚拟头节点的方法来使得规则一致。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res=cur=ListNode(-1)#定义虚拟头节点和临时节点
        res.next=head#将虚拟头节点指向head
        while cur.next:#遍历临时节点
            if cur.next.val==val:#当下一个节点的值等于要删的值，跳过下一个节点
                cur.next=cur.next.next
            else:#否则正常添加
                cur=cur.next
        return res.next#返回虚拟头节点的下一个节点。
