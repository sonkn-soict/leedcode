import signal
import time 
TIME_LIMIT = 10

def handler(signum, frame):
    raise TimeoutError("Time limit exceeded")
signal.signal(signal.SIGALRM, handler)
signal.alarm(TIME_LIMIT)

# Partition
# Move zeroes to the beginning of the list and ones to the end of the list.
def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    return nums
nums = [0,1,0,1,1,0,0,1]
result = move_zeroes(nums)
print(result)

signal.alarm(0) # Disable the alarm