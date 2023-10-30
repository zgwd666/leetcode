#https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
'''
解题思路：
利用双指针方法循环迭代
具体方法为：
创建结果指针指向head，然后获取链表的长度
然后创建指针指向结果指针，遍历到位置
然后跳过指定位置，输出结果指针的下一位
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res=ListNode(0)#创建结果指针并给一个初始化节点
        res.next=head#结果指针指向输入链表
        cur,length=head,0#创建指针指向输入链表，初始化长度
        while cur:#遍历链表，获取链表的长度
            length+=1
            cur=cur.next
        cur=res#将指针指向结果指针
        for i in range(length-n):#遍历到指定位置的前一位置停止
            cur=cur.next
        cur.next=cur.next.next#跳过指定位置的结点
        return res.next#输出结果
