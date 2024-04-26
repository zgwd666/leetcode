#https://leetcode.cn/problems/gas-station/
'''
解题思路：如果总油量减去总消耗大于等于0那么一定可以跑完一圈，说明各个站点的加油站剩油量rest[i]相加一定是大于等于0的。

各个加油站的剩余量等于gas[i]-cost[i]

i从0看i是累加rest[i]，和记为curSum，一旦curSum小于0，说明[0,i]区间都不能作为起始位置，因为这个区间选择任何一个位置作为起点，到i这里都会断油，那么起始位置从i+1开始算起，再从0计算curSum。
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curGas=0#当前累计的剩余油量
        totalGas=0#初始化跑完一圈之后剩余的总油量
        start=0#初始化开始索引
        for i in range(len(gas)):#对每个加油站进行遍历
            curGas+=gas[i]-cost[i]#计算当前累计的剩余油量
            totalGas+=gas[i]-cost[i]#计算总剩油量
            if curGas<0: # 当前累计剩余油量curSum小于0
                start=i+1 # 起始位置更新为i+1
                curGas=0 # curGas重新从0开始累计
        if totalGas<0:
            return -1# 总剩余油量totalSum小于0，说明无法环绕一圈
        return start
