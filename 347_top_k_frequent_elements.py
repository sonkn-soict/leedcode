import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Docstring for topKFrequent
        
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dict = {}
        pq = []
        result = []
        for key in nums:
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1
        for key in dict:
            heapq.heappush(pq,(-dict[key], key))
        for i in range(k):
            _, task = heapq.heappop(pq)
            result.append(task)
        return result

nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
Res = Solution()
result = Res.topKFrequent(nums, k)
print(result)