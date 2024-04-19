#https://leetcode.cn/problems/palindrome-partitioning/
'''
解题思路：采用回溯的思路，对字符串进行分割。
在进行回溯的时候，递归用来纵向遍历，for循环用来横向遍历。切割线切割到字符串的结尾位置，说明找到一个切割方法。
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
         # 初始化一个空列表，用于存储分割的结果
        result=[]
         # 定义一个深度优先搜索(dfs)的内部函数，用于递归地分割字符串
        def dfs(s,index,path,result):
            # 当前索引index等于字符串s的长度时，说明已经到达字符串的末尾
            if index==len(s):
                # 将当前路径path添加到结果列表result中
                result.append(path[:])
                 # 直接返回，结束这次递归
                return
            # 从当前索引index开始，尝试分割字符串s
            for i in range(index,len(s)):
                # 检查从当前索引到i的子字符串是否为回文
                if s[index:i+1]==s[index:i+1][::-1]:
                    # 如果是回文，将其添加到当前路径path中
                    path.append(s[index:i+1])
                    # 递归调用dfs函数，将索引设置为i+1，继续分割剩余的字符串
                    dfs(s,i+1,path,result)
                    # 回溯，移除当前路径path中的最后一个元素
                    path.pop()
         # 调用dfs函数，从字符串s的索引0开始，初始化路径path为空列表，结果列表result
        dfs(s,0,[],result)
        # 返回分割结果
        return result
