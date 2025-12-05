from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        for i in range(n):
            for j in range(i+1, n):
                length = j - i
                width = min(heights[i], heights[j])
                res = max(res, length*width)
        return res
    def maxArea_v2(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)

        l, r = 0, n-1
        while l < r:
            res = max(res, (r-l)*min(heights[l], heights[r]))
            if heights[l] > heights[r]: r -= 1
            else: l += 1
        return res