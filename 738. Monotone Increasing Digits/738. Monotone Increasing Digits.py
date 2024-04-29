#https://leetcode.cn/problems/monotone-increasing-digits/
'''
解题思路：对n进行判断，如果是，直接返回n,不是的话找到第一个不是单调递增的元素，将其前面的元素减一，然后把后面的元素全部置为9.
'''
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n<10:return n#小于10的数字天生满足田间
        def helper(n):#判断n是否为单调递增，不是的话返回哪一个位置开始不满足
            n=str(n)
            for i in range(1,len(n)):
                if int(n[i])<int(n[i-1]):
                    return i,False
            return 0,True
        while True:#对n进行遍历
            index,flag=helper(n)
            if flag:
                return n
            else:#如果n不是单调递增，则将n的第一个不满足单调递增规则后面的元素全部置为9，将该位置的数字减一
                n=str(n)
                front=int(n[:index+1])
                front-=1
                n=str(front)+'9'*(len(n)-index-1)
                n=int(n)
