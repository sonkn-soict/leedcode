class Solution(object):
    def maximunTripletValue(self, nums):
        """
        Docstring for maximunTripletValue
        
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3: 
            return 0
        prefix_max, stuffix_max = self.prefix_max(nums), self.stuffix_max(nums) 
        result = 0
        for i in range(1, n-1):
            print(prefix_max[i-1], nums[i], stuffix_max[i+1])
            result = max(result, (prefix_max[i-1] - nums[i]) * stuffix_max[i+1])
        return result
    def stuffix_max(self, nums):
        n = len(nums)
        result = [nums[n-1]] * n
        for i in range(n-2, -1, -1):
            result[i] = max(nums[i], result[i+1])
        
        return result
    
    def prefix_max(self, nums):
        n = len(nums)
        result = [nums[0]] * n
        for i in range(1, n):
            result[i] = max(nums[i], result[i-1])
        
        return result

nums = [1,10,3,4,19]

res = Solution()
result = res.maximunTripletValue(nums)
print(result)