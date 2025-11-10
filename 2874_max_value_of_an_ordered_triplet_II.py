class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        max_value = 0
        prefix_max = self.prefix_max(nums)
        print(prefix_max)
        suffix_max = self.suffix_max(nums)
        print(suffix_max)
        print(nums)
        print(len(nums))
        for i in range(1, len(nums) - 1):
            print(f"Max value: {max_value}, prefix: {prefix_max[i - 1]}, suffix_max: {suffix_max[i + 1]}")
            max_value = max(max_value, (prefix_max[i - 1] - nums[i]) * suffix_max[i + 1])
        return max_value

    def prefix_max(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]
        prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = max(prefix[i - 1], nums[i])
        return prefix
    def suffix_max(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]
        suffix = [nums[-1]] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], nums[i])
        return suffix
    
nums = [1000000,1,1000000]
result = Solution()
res = result.maximumTripletValue(nums)
print(res)  
