from typing import List
class Solution:
    # 1. Create prefix and suffix map
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix, stuffix = self.prefix_products(nums, n), self.stuffix_products(nums, n)
        for i in range(n):
            if i == 0:
                res[i] = stuffix[1]
            elif i == n-1:
                res[i] = prefix[n-2]
            else:
                res[i] = prefix[i-1]*stuffix[i+1]  
        return res
    def prefix_products(self, nums: List[int], n) -> List[int]:
        if n < 2:
            return nums
        res = [nums[0]] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i]
        return res
    def stuffix_products(sefl, nums: List[int], n) -> List[int]:
        if n < 2:
            return nums
        res = [nums[n-1]] * n
        for i in range(n-2, -1, -1):
            res[i] = res[i+1] * nums[i]
        return res
    
    # 2. On^2 => 2 loops to caculate 

    # 3. Better prefix and suffix
    def productExceptSelf_v2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1]*suffix[i+1]
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res
    
    # 4. Optimal prefix and suffix
    def productExceptSelf_v3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res
    
nums = [1,2,4,6]
sol = Solution()
res = sol.productExceptSelf(nums)
print("res",res)
res_v2 = sol.productExceptSelf_v2(nums)
print("res_v2", res_v2)
res_v3 = sol.productExceptSelf_v3(nums)
print("res_v3", res_v3)
