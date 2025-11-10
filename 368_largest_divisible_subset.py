class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        print(nums)
        arr = self.sort(nums)
        print(arr)
        dict_divisible = {}
        max_arr = []
        for i in range(len(arr)):
            dict_divisible[arr[i]] = []
            for j in range(i+1, len(arr)):
                if arr[j] % arr[i] == 0:
                    dict_divisible[arr[i]].append(arr[j])    
                continue   
        
        for key in dict_divisible:
            arr = [key]
            for 
            


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
                j -= 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

nums = [1,2,3,4,6,8]
res = Solution()
result = res.largestDivisibleSubset(nums)

print(result)