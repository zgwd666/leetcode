#https://leetcode.cn/problems/climbing-stairs/description/
'''
解题思路：
当n为1时，方法为1
当n为2时，方法为2
当n为3时，方法为（从一阶直接到三阶方法一种，从二阶直接到三阶方法一种）3（3=一阶本身的方法1+二阶本身的方法2）
当n为4时，方法为（从二阶直接到四阶方法一种，从三阶直接到四阶方法一种）5（5=二阶本身的方法2+三阶本身的方法3）
依次类推，可以得到，递推公式为f(n)=f(n-1)+f(n-2) f(0)=1 f(1)=1
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:#如果只有一阶台阶，那方法只有一种
            return 1
        a=b=1#设置初始值，也就是设置 f(0)=1 f(1)=1
        for i in range(2,n+1):
            a,b=b,a+b#进行迭代,也就是执行f(n)=f(n-1)+f(n-2) 公式
        return b
