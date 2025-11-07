import time
import signal

TIME_LIMIT = 10
def handler(signum, frame):
    raise TimeoutError("Time limit exceeded")
signal.signal(signal.SIGALRM, handler)
signal.alarm(TIME_LIMIT)

# one point start slow, one point fast
# Detete duplicate from sorted array
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
nums = [1,1,2,2,3,4,4,5]
length = remove_duplicates(nums)
print(length)
print(nums[:length])



signal.alarm(0)  # Disable the alarm