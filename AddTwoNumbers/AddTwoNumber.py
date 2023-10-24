#https://leetcode.cn/problems/add-two-numbers/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
解题思路：
将两个链表从表头开始取值相加，因为值的范围在0-9之间，相加不会超过20，所以只需要考虑前面的相加的数是否大于10，如果大于10，则将个位数记作本位置的数，十位上的数字带入下一位置计算，直到两个遍历完成为止。
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=cur=ListNode(-1)#创建一个普通指针和哑变量，普通变量用于遍历产生新的结点，哑变量始终指向链表的头部
        s=0#初始化一个值
        while l1 or  l2 or s:
            s+=(l1.val if l1 else 0)+(l2.val if l2 else 0)#进行相加，就是将上一层的十位数上的值+本位置上的l1值（如果存在的话）+本位置上的l2的值(如果存在的话)
            cur.next=ListNode(s%10)#将值的个位数的值作为本位置的结点值
            cur=cur.next#结点向前移动
            s//=10#获取值的十位上的值带入下一位置的计算
            l1=l1.next if l1 else None#l1结点前移
            l2=l2.next if l2 else None#l2结点前移
        return res.next#返回相加后的链表。
            
