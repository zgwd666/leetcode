#https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
'''
解题思路：采用双指针的方式，先将二者按末尾对齐，然后同时向后遍历，寻找交点
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengthA,lengthB=0,0#初始化两个链表的长度
        cur=headA#临时节点指向headA
        while cur:#遍历headA链表
            lengthA+=1#长度+1
            cur=cur.next#向后移动
        cur=headB#临时节点指向headB
        while cur:#遍历headB链表
            lengthB+=1#长度+1
            cur=cur.next#向后移动
        curA,curB=headA,headB#定义临时节点分别指向headA和headB
        if lengthA>lengthB:#为了方便计算，我们统一将较长的链表定义为curB
            curA,curB=curB,curA
            lengthA,lengthB=lengthB,lengthA
        for _ in range(lengthB-lengthA):#将curB与curA进行尾部对齐
            curB=curB.next
        while curB:#遍历两个链表，因为此时curB和curA的长度一致，所以判断条件为curA或curB效果是一样的
            if curB==curA:#二者相等，返回交点
                return curB
            else:#二者不等，则同时向后遍历
                curB=curB.next
                curA=curA.next
        return None#没找点交点，返回None
