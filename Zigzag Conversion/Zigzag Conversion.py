#https://leetcode.cn/problems/zigzag-conversion/description/
'''
解题思路：
Z字形的数组可以将其填充为N行重复的字符串，然后选择特定的字符
以字符串为ABCDEFGH ，numRows为3为例进行说明,可以改写为：
A    E
 B  D  F  H
  C     G
上面的可以进行填充
ABCDEFGH
ABCDEFGH
ABCDEFGH
可以发现的规律为：第0行取第0个；第1行取第1个；第2行取第2个；第3行取第numRow-1个，....
可以发现在第0行之后取的方向和第numRow-1之后取得方向是相反的。
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #如果只有一行，直接返回即可
        if numRows<=1:
             return s
        #创建n个s组成的列表，对应上面的填充字符串
        l1=[s for i in range(numRows)]
        #定义行索引
        flag=0
        #定义方向索引
        direction=1
        #创建空列表，用于返回Z字形的字符串
        l2=[list() for i in range(numRows)]
        #创建空字符串用于返回最终的结果
        s2=''
        #对填充字符串列表进行遍历，以获得Z字形的字符串
        #先按照顺序进行取，遇到最后一行和最开始的行就调转方向直到把字符串遍历完成为止
        for j in range(len(s)):
            l2[flag].append(l1[flag][j])
            flag+=direction
            if flag==0 or flag==numRows-1:
                direction*=-1
        #遍历完成的l2是一个二维列表，将其遍历，将字符拼接为新的字符串
        for i in l2:
            for j in range(len(i)):
                s2+=i[j]

        return s2

