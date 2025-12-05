class Solution(object):
    def hasDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        result = set()
        for i in range(n):
            result.add(nums[i])
        if len(result) != n:
            return True
        else:
            return False
    
    def hasDuplicated_best(self, nums: list[int]) -> bool:
        return len(set(nums) < len(nums))
nums = [1, 2, 3, 3]

res = Solution()
result = res.hasDuplicate(nums)
print(result)
