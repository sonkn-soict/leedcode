from typing import List

class Solution:
    # 1. Check each num: Brute Force 
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0 
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            res = max(res, streak)
        
        return res
    
    # 2. Sorting
    def longestConsecutive_v2(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        nums.sort()
        res, streak, curr, i = 0, 0, nums[0], 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)            

        return res
    
    # 3. Hash set
    def longestConsecutive_v3(self, numsL: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums: 
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                res = max(res, length)
        
        return res
nums = [2,20,4,10,3,4,5]
sol = Solution()
res = sol.longestConsecutive(nums)
res_v2 = sol.longestConsecutive_v2(nums)
res_v3 = sol.longestConsecutive_v3(nums)
print("res", res)
print("res_v2", res_v2)
print("res_v3", res_v3)