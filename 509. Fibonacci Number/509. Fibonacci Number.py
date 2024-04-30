#https://leetcode.cn/problems/fibonacci-number/
'''
解题思路：可以采用回溯的方法
'''
class Solution:
    def fib(self, n: int) -> int:
        if n<2:return n#确定回溯终止条件
        return self.fib(n-1)+self.fib(n-2)#计算结果
