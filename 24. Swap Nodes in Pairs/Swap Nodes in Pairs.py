#https://leetcode.cn/problems/swap-nodes-in-pairs/
'''
思路，两两交换链表节点，需要定义一个虚拟头节点进行辅助
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head#先进行判断，小于两个元素的链表不需要进行操作
        dummy_head=ListNode(-1)#定义虚拟头节点
        cur=dummy_head#定义临时节点
        dummy_head.next=head#将虚拟头节点指向head
        while cur.next and cur.next.next :#进行遍历，需要下一个元素和下下个元素存在
            temp=cur.next#存储待向后交换节点
            temp1=cur.next.next.next#存储交换后节点指向的节点
            cur.next=temp.next#将虚拟头节点指向待向前交换的节点
            cur.next.next=temp#将虚拟头节点的下一个节点指向待向后交换的节点
            temp.next=temp1#将待向后交换的节点指针指向第三个节点。
            cur=cur.next.next#移动cur节点
        return dummy_head.next
