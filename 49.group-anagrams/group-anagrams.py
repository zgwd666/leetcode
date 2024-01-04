#https://leetcode.cn/problems/group-anagrams/description/
'''
解题思路：采用哈希的方式将字母异位词 组合在一起
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<2:return [strs]#当数组内为空或仅有一个元素，返回[strs]
        dict1={}#建立哈希表
        for i in strs:#进行遍历
            key=str(sorted(i))#sorted的结果类型为list，需要重新转换为str，哈希函数就是将元素转换为有序元素
            if key in dict1.keys():#哈希表中存在索引，则添加
                dict1[key].append(i)
            else:#哈希表中存在索引，则新建
                dict1[key]=[i]
        res=[lst for lst in dict1.values()]#将哈希表的值转换为二位列表
        return res#返回结果
