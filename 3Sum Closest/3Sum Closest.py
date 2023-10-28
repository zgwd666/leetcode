#https://leetcode.cn/problems/3sum-closest/description/
'''
解题思路：
采用双指针的思路。
先将数组进行升序排列。定义两个双指针分别指向当前位置的下一个位置和数组末尾的位置。
进行遍历直到两个指针进行重合：
当遍历时，计算三者的和、与target的差：
1.相等：直接返回和也就是target的值
2.差小于0，证明此时三者加和小了，将左指针向右移动
3.差大于0，证明此时三者加和大了，将右指针向左移动
在移动的过程中不断的进行当前差值和之前差值的比较，并与target最近的和
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)<=3:#当输入的数组里面的数小于等于3时，直接返回加和
            return sum(nums)
        res=0#初始化最终的结果
        min_dist=1e6#初始化全局最小距离，要给大一些，才能更新的动
        nums=sorted(nums)#将数组进行升序排列
        for i in range(len(nums)):#进行遍历
            l=i+1#定义左指针
            r=len(nums)-1#定义右指针
            while l<r:#进行遍历直到左右指针重合
                s=nums[i]+nums[l]+nums[r]#计算三者的和
                cur_dist=s-target#计算当前和与target的距离
                if cur_dist==0:#当距离为0，直接返回当前的和
                    return s
                elif cur_dist<0 :#当距离小于0，左指针向右移动
                    l+=1
                    if abs(cur_dist)<min_dist:#全局最小距离为了统一，进行正数的对比，如果当前的距离小于之前的距离，和进行更新
                        min_dist=abs(cur_dist)
                        res=s
                else:#当距离大于0，右指针向左移动
                    r-=1
                    if cur_dist<min_dist:#如果当前的距离小于之前的距离，和进行更新
                        min_dist=cur_dist
                        res=s
        return res
                    
