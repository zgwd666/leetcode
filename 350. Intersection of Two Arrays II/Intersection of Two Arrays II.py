#https://leetcode.cn/problems/intersection-of-two-arrays-ii/
'''
解题思路：本题需要考虑重复的元素，那么就采用以第一个列表为准，如果第二个列表中的元素在第一个中，则加入结果数组，并且删除第一个列表中的第一次出现该元素的位置。
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:return []#如果存在空数组，则交集一定为空
        res=[]#定义结果列表
        for i in range(len(nums2)):#遍历第二个列表
            if nums2[i] in nums1:#如果第二个列表中的元素在第一个中，则加入结果数组，并且删除第一个列表中的第一次出现该元素的位置。
                res.append(nums2[i])
                nums1.remove(nums2[i])
        return res
