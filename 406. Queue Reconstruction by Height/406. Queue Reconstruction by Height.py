#https://leetcode.cn/problems/queue-reconstruction-by-height/
'''
解题思路：在本题中，首先对数据进行排序，按照数对的元素1降序，按照数对的元素2升序。原因是，按照元素1降序排序，对于每个元素，在其之前的元素个数，就是大于等于它的元素的数量，而按照第二个元素正向排序，我们希望k大的尽量在后面，减少插入操作的次数。
'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue=[]
        # 先按照h维度的身高顺序从高到低排序。确定第一个维度
        # lambda返回的是一个元组：当-x[0](维度h）相同时，再根据x[1]（维度k）从小到大排序
        people.sort(key=lambda x:(-x[0],x[1]))
        # 根据每个元素的第二个维度k，贪心算法，进行插入
        # people已经排序过了：同一高度时k值小的排前面。
        for p in people:
            queue.insert(p[1],p)
        return queue
