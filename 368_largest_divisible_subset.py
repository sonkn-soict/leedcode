class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1. Sort
        if not nums:
            return []

        arr = self.sort(nums)
        n = len(arr)

        # 2. dp[i] = length of largest divisible subset that ends at i
        dp = [1] * n
        parent = [-1] * n # parent[i] = index of previois element in the subset at i

        max_len = 1
        max_idx = 0

        # 3. Compute dp
        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    # if extend subset ending at j gives longer subset ending at i
                    if dp[j] + 1 > dp[i]:        
                        dp[i] = dp[j] + 1
                        parent[i] = j
                
            # trach the overall maximum:
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i
        res = []
        cur = max_idx
        while cur != -1:
            res.append(arr[cur])
            cur = parent[cur]
        
        return res


    def sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.sort(nums[:mid])
        right = self.sort(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else: 
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

nums = [1,2,3,4,6,8]
res = Solution()
result = res.largestDivisibleSubset(nums)

print(result)