#https://leetcode.cn/problems/partition-labels/
'''
解题思路：
先确定思路：看见开头一个字母，就要看这个字母最后出现在哪，然后康康这个开头和结尾之间的那些其他字母是不是都落在这个区间里，
如果不是，则扩充区间，如果是，那就最好了ww。
对于这道题，一个关键点是利用字典key的唯一性来记载一个字母最大的index是几。
然后，遍历字符串并跟它比较，用max函数来康康是边界大还是当前遍历的这个字母的最大index大，
如果当前遍历字母的最大index大，那就说明超过了边界，那就要更新边界，大概就是这个思路。
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s)==1:return [1]#返回特殊情况
        dict1={}#初始化一个哈希表，用于存储字符对应的最大下标
        for i in range(len(s)):#遍历字符串，存储每个字符的最大下标
            dict1[s[i]]=i
        start=0 # 起始边界， 
        result=[]
        end=0#结束边界
        for i,ch in enumerate(s):
            end=max(end,dict1[ch])# 这里就是用边界和当前遍历到的那个字母的最大index去比较，看看谁大，如果最大index大就扩充边界。
            if i==end:
                result.append(end-start+1) # 最后，遍历的位置和边界重合了，那就ok了，从这里截断并记录长度。
                start=i+1
        return result
