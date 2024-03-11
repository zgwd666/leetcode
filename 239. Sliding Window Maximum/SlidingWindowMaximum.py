#https://leetcode.cn/problems/sliding-window-maximum/?envType=study-plan-v2&envId=top-100-liked
'''
解题思路：利用单调队列来做
单调队列的概念就是队列中从小到大的顺序进行排序
具体到本题，实现的思路是
先初始化一个双端队列，然后第一个元素入队，之后元素依次入队，如果待入队元素比队中最后一个元素大，则之前的元素全部弹出，
待入队元素入队。同样超过窗口距离的元素从左侧出队，记录每个窗口的第一个元素。
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:return []#如果k为0或nums为空，则直接返回空
        n=len(nums)#获取数组长度
        deque=collections.deque()#实例化双端队列
        res=[]#初始化结果数组
        for i in range(k):#先遍历第一个窗口内的元素
            while deque and deque[-1]<nums[i]:#队非空且待入队元素比队中最后一个元素大，
                deque.pop()#则弹出之前所有的元素
            deque.append(nums[i])#将待入队元素入队
        res.append(deque[0])#第一个元素就是最大的元素，添加到结果数组中
        for i in range(k,n):#遍历之后的数组
            if deque[0]==nums[i-k]:#将超出窗口范围的元素从队列左侧出队
                deque.popleft()
            while deque and deque[-1]<nums[i]:#队非空且待入队元素比队中最后一个元素大，
                deque.pop()#则弹出之前所有的元素
            deque.append(nums[i])#将待入队元素入队
            res.append(deque[0])#第一个元素就是最大的元素，添加到结果数组中
        return res
