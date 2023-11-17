'''
解题思路：采用字符串和数字之间相互转换，时间复杂度为O(n)
先把数组中的数字全部读取到一个字符串中，然后将字符串转换为整数，之后整数+1.转换回字符串，将每一个字符转换为整数加入到数组中。
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)#获取数组长度
        s1=''#创建字符串用于接受数组中的元素
        for i in range(n):#进行遍历，将数组中的每一个元素转换为字符然后加入到字符串中
            s1+=str(digits[i])
        s1=int(s1)#将整数字符串转换为整数
        s1+=1#整数+1
        s2=str(s1)#将结果整数重新转换为整数字符串
        res=[]#初始化结果数组
        for i in range(len(s2)):#进行遍历，将字符串中的每个元素转换为整数后加入数组
            res.append(int(s2[i]))
        return res
