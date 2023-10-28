#https://leetcode.cn/problems/3sum/description/
'''
解题思路：
利用双指针来解题。
先将数组从小到大进行排序，然后对数组中的元素进行遍历：
在遍历时，加入遍历的当前元素>0，则直接返回
否则的话，定义两个指针，一个用于指向当前位置的下一个位置，另一个用于指向数组的末尾，三者相加，会出现以下三种情况：
1.相加正好等于0：则将当前的数组加入解中，同时需要跳过重复解，然后指针向内移动
2.大于0，则证明右侧的数太大了，将右指针向左移动
3.小于0，则证明左侧的数太小了，将左指针向右移动
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        l1=sorted(nums)
        res=[]
        for i in range(len(l1)):
            if l1[i]>0:
                return res
            if i>0 and l1[i]==l1[i-1]:
                continue
            l=i+1
            r=len(l1)-1
            while l<r:
                if l1[i]+l1[l]+l1[r]==0:
                    res.append([l1[i],l1[l],l1[r]])
                    while l<r and l1[l]==l1[l+1]:
                        l+=1
                    while l<r and l1[r]==l1[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif l1[i]+l1[l]+l1[r]>0:
                    r-=1
                else:
                    l+=1
        return res

                    

            

