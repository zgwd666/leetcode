#https://leetcode.cn/problems/intersection-of-two-arrays/
'''
解题思路：采用哈希的方式，求出每个数组的不重复的元素，求二者交集即可
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:return []#如果存在空数组，则交集一定为空
        dict1={}#定义一个数组的字典，存储第一个数组中不重复的元素
        dict2={}#定义一个数组的字典，存储第二个数组中不重复的元素
        for i in range(len(nums1)):#遍历第一个数组
            if nums1[i] not in dict1:#如果元素不在字典的keys集合，添加
                dict1[nums1[i]]=1
        for i in range(len(nums2)):#遍历第二个数组
            if nums2[i] in dict1:#如果元素存在第一个字典的keys集合中，就是二者的交集，添加到第二个字典的keys集合中，但是只添加一次
                dict2[nums2[i]]=1
        res=list(dict2.keys())#将keys集合转换为列表
        return res#返回结果
