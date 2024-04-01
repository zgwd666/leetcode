#https://leetcode.cn/problems/top-k-frequent-elements/
'''
解题思路：采用字典存储各个元素的出现频率，再根据字典的value次数进行排序，最后取数组的前k个元素
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}#初始化字典
        for i in range(len(nums)):#对数组进行遍历,采用字典存储各个元素的出现频率
            if nums[i] in dict1:
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        sort_res=sorted(dict1,key=lambda x:dict1[x],reverse=True)#再根据字典的value次数进行排序
        return sort_res[0:k]#取数组的前k个元素
