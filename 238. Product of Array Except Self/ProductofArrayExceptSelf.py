#https://leetcode.cn/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-100-liked
'''
求除自身的数组元素的乘积，就可以将其分为元素位置左方和元素位置右方两部分
乘积等于左边前缀连乘数组乘以右边前缀连续数组
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)#获取长度
        res=[0]*n#初始化结果数组
        mul=1#初始化乘积
        for i in range(n):
            res[i]=mul#将左边前缀连乘存入结果数组中
            mul*=nums[i]#计算左边前缀连乘
        mul=1
        for i in range(n-1,-1,-1):#反方向遍历数组
            res[i]*=mul#计算结果
            mul*=nums[i]#计算右边前缀连乘
        return res
