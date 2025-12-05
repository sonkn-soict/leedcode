from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        suffix = [0] * n
        suffix[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = max(prices[i], suffix[i+1])
        for i in range(n-1):
            res = max(res, suffix[i+1]-prices[i])

        return res
    
    # 2. Two points
    def maxProfit_v2(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
            else: 
                l = r
            r += 1
        
        return res
