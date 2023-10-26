#https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
'''
解题思路：
滑动窗口法：利用两个指针，第一个指针指向头部，第二个指针指向尾部，二者之间的区域就是一个窗口。
针对本题而言，先定义一个i=j=0，先将第一个元素存放到存储列表中，然后保持i不懂，j向后移动，直到碰到和相同的元素为止。
当碰到相同的元素，先通过本次的长度和之前的最长长度进行对比，获得新的最长长度，然后将i移动到存储列表中的相同元素的位置，然后将相同位置添加到存储列表的末尾，并移动J
重复上述过程，直到j到达末尾
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:#输入空字符串，那么无重复字符的最长子串的长度为0
            return 0
        l1=[]#定义存储列表
        max_len=0#定义最大长度
        cur_len=0#定义当前长度
        for  i in range(len(s)):#进行遍历
            val=s[i]#获取当前字符
            if val not in l1:如果当前字符没有在存储列表中出现，也就是还未重复，将当前字符添加到列表中，当前长度加1
                l1.append(val)
                cur_len+=1
            else:#如果重复了，就将列表中的重复字符及之前的元素丢弃，并在列表中重新添加上当前字符，并获取当前长度
                index=l1.index(val)
                l1=l1[index+1:]
                l1.append(val)
                cur_len=len(l1)
            if cur_len>max_len:#进行最大长度更新。
                max_len=cur_len
        return max_len

        
