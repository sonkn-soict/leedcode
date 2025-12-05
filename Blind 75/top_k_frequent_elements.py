class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in  nums:
            count[i] = 1 + count.get(i, 0)
        # sort the count dict by value
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_count[i][0])
        return res
        