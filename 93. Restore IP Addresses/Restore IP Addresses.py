#https://leetcode.cn/problems/restore-ip-addresses/
'''
解题思路：采用深度优先搜索（DFS）的算法来解决恢复IP地址的问题。它通过递归地尝试字符串 `s` 的每一个可能的分割方式，来构建潜在的IP地址段。在每次递归调用中，它检查当前的子字符串是否为一个有效的IP地址段（即不以0开头，且为1到3位数字，且整体在0到255的范围内）。如果当前段有效，它将继续递归处理剩余的字符串，直到构建出所有可能的、有效的IP地址。当递归到达第四段且字符串已经完全处理完毕时，当前路径（去掉最后一个点）将作为一个有效的IP地址被添加到结果列表中。最终，这个列表包含了所有根据给定字符串 `s` 构造出的合法IP地址。
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s and len(s)<4:return []# 特殊情况处理
        result=[] # 初始化结果列表
           # DFS递归，s为目标字符串，index为对s的分割次数（也是递归深度），path为划分的中间（最终）结果字符串，result为结果列表
        def dfs(s,index,path,result):
            # 如果index大于4，那么说明字符串s已经被分割的次数大于4，此时直接返回
            if index>4:
                return
             # 如果index等于4，那么还要继续判断递归传入的s是否已经为空，如果s为空则说明字符串已经被完全分割为IP地址的形式，此时将该分割方法（路径）存储到结果列表result中，然后返回
            if index==4 and not s:
                # 这里符合条件的path的形式应该是"xxx.xxx.xxx.xxx."，因此path[:-1]是为了舍弃最后的'.'字符
                result.append(path[:-1])
                return
            # 对s的下标进行遍历
            for i in range(len(s)):
                # 后面的if语句用于处理以下两种情况：
                 # （1）当s的首字符为'0'时，可以直接将'0'作为IP地址中四个整数之一
                 # （2）当s的首字符不为'0'时，需要保证s[:i+1]处于IP地址整数的范围之内
                if s[:i+1]=='0' or(s[0]!='0' and 0<int(s[:i+1])<256):
                # DFS递归调用的参数需要进行以下操作：
                # （1）将下标i之后的s[i+1:]字符串作为新的s进行递归参数传入
                # （2）分割次数idx+1
                # （3）将中间字符串结果path后连接下标i之前的s[:i+1]字符串，并在最后加入'.'
                # （4）结果列表res依然原封不动的传入下次递归
                    dfs(s[i+1:],index+1,path+s[:i+1]+'.',result)
        dfs(s,0,'',result)# DFS递归，需要传入字符串s，对s的分割次数（初始为0），划分的中间（最终）结果，最终结果列表res
        
        return result
