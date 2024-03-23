# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:return head
        cur,pre=head,None#初始化 cur初始化head，pre为head之前也就是None
        while cur:#遍历 知道遍历到None 也就是遍历完链表的时候结束遍历
            temp=cur.next#需要一个临时指针保存cur的下一个指针
            cur.next=pre#进行赋值 cur的指针指向pre
            pre=cur#移动pre
            cur=temp#cur移动到下一个
        return pre
