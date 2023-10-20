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
        #创建一个新的链表，里面有一个结点，值为-1，定义两个指针，其中res为哑变量，保持指向不变，指向链表的开始；cur为普通指针，用来不断添加新结点
        res=cur=ListNode(-1)
        #对两个链表进行遍历，直到遍历到一个链表的末尾为止
        while list1 and list2:
            #如果list1的值大于list2的值，则将list2的值赋给cur的指针的下一位置，同时将list2的指针指向下一位置
            if list1.val>list2.val:
                cur.next=list2
                list2=list2.next
            #如果list1的值小于list2的值，则将list1的值赋给cur的指针的下一位置，同时将list1的指针指向下一位置
            else:
                cur.next=list1
                list1=list1.next 
            #将cur的指针移到下一个位置
            cur=cur.next
        #如果链表不等长，将剩余链表的剩余值赋给cur的下一位置
        cur.next=list1 if list1 else list2
        #将哑指针的位置前移，指向链表真正的开始
        return res.next
