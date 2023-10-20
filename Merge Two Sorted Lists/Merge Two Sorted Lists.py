#https://leetcode.cn/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        输入：
        list1：链表1
        list2：链表2
        输出：
        按顺序排列的合并的链表
        '''
        #先进行判断list1和list2是否为空，list1为空输出list2，list2为空输出list1，二者都为空就输出list2也就是[]
        if not list1:
            return list2
        if not list2:
            return list1
        #创建一个新的链表，里面有一个结点，值为-1，定义两个指针，其中res为哑变量
        res=cur=ListNode(-1)
        while list1 and list2:
            if list1.val>list2.val:
                cur.next=list2
                list2=list2.next
            else:
                cur.next=list1
                list1=list1.next 
            cur=cur.next
        cur.next=list1 if list1 else list2
        return res.next
