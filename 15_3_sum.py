class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = self.sort(nums)
        print(arr)
        result = []
        for i in range(len(arr)):
            if i != 0 and arr[i] == arr[i-1]:
                continue
            left, right = i+1, len(arr) -1
            while left < right:
                if left != i+1 and arr[left] == arr[left - 1]:
                    left += 1
                    continue
                if right != (len(arr) - 1) and arr[right] == arr[right + 1]:
                    right -= 1
                    continue

                total = arr[left] + arr[right] + arr[i]
                if total == 0:
                    result.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else: 
                    left += 1
        return result

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

nums =[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]

res = Solution()
result = res.threeSum(nums)
print(result)
