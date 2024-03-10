#https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：
字母的异位词，不管怎么排列，它们其中各个字母的数量是一致的，所以可以采用对比字母数量的方法判断两个词是不是异位词
具体来说就是：
对长字符串和标准字符串建立一个字母的映射，也就是hashmap，然后求得标准字符串的字母映射，在对比长字符串串中对应
长度的字串的字母映射是否与其一致。
在这个过程中，为了优化时间复杂度，在求标准字符串的映射时可以求长字符串的第一个字串的映射。
然后后续每次只需要在前一个字串的基础上删除第一个字符，添加尾部一个字符，进行判断即可
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):return []#进行简答判断，长字符串小于标准字符串不需要判断，直接返回空
        res=[]#初始化结果数组
        p_cnt=[0]*26#初始化标准字符串的hashmap
        s_cnt=[0]*26#初始化长字符串的字串的hashmap
        n,m=len(s),len(p)#获取长字符串、标准字符串长度
        for k in range(m):#对标准字符串进行遍历同时对长字符串第一个字串进行遍历
            p_cnt[ord(p[k])-ord('a')]+=1#获取标准字符串的hashmap
            s_cnt[ord(s[k])-ord('a')]+=1#获取长字符串第一个字符串的hashmap
        if p_cnt==s_cnt:#进行判断，如果一致则添加0
            res.append(0)
        for i in range(1,n-m+1):#对长字符串剩下字串进行遍历
            s_cnt[ord(s[i-1])-ord('a')]-=1#去掉前一个字符
            s_cnt[ord(s[i+m-1])-ord('a')]+=1#在尾部添加一个字符
            if s_cnt==p_cnt:#进行判断，如果一致添加起始索引
                res.append(i)
        return res
