#https://leetcode.cn/problems/lemonade-change/
'''
解题思路：
存在如下的情况：
- 情况一：账单是五，直接收下
- 情况二：账单是十，消耗一个五，增加一个十
- 情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5.
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0#记录五块钱的数量
        ten=0#记录十块钱的数量
        for b in bills:#进行遍历
            if b==5:#账单是五，直接收下，增加一个5
                five+=1
            elif b==10:#账单是十，消耗一个五，增加一个十
                five-=1
                ten+=1
            elif b==20:#账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5.
                if ten>0:
                    ten-=1
                    five-=1
                else :
                    five-=3
            if five<0:#判断五块钱是否支撑上面的消耗，如果不，直接返回False
                return False
        return True#遍历完成且未出现不够的情况，返回True
