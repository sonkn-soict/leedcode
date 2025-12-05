class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None
        
    def twoSum_sorted(self, nums: list[int], target: int) -> list[int]:
            A = []
            for i, num in enumerate(nums):
                A.append([num, i])

            A.sort()
            i, j = 0, len(nums) - 1
            while i < j:
                cur = A[i][0] + A[j][0]
                if cur == target:
                    return [min(A[i][1], A[j][1]),
                            max(A[i][1], A[j][1])]
                elif cur < target:
                    i += 1
                else:
                    j -= 1
            return []
    
    def twoSum_hashmap(self, nums: list[int], target: int) -> list[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []
    def twoSum_hashmap_best(self, nums: list[int], target: int) -> list[int]:
        indicate = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in indicate:
                return [indicate[diff], i]
            indicate[num] = i