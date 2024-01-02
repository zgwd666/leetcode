#https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
解题思路：采用遍历的方式，跳过重复的元素即可
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=ListNode(-1)
        cur.next=head#初始化一个节点，指向head
        while head:#进行遍历
            if head.next is not None:
                if head.val==head.next.val:#如果head的下一个不为None且与当前节点的val相同，跳过；否则正常遍历
                        head.next=head.next.next
                else:
                     head=head.next
            else:
                head=head.next
        return cur.next 
