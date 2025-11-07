# Opposite Ends
# One point is at the start of the list and the other is at the end of the list.
# The two points move toward each other until they meet in the middle.


# setup time limit for all script 100s

import time
import signal

TIME_LIMIT = 10
def handler(signum, frame):
    raise TimeoutError("Time limit exceeded")
signal.signal(signal.SIGALRM, handler)
signal.alarm(TIME_LIMIT)

def two_sum_sorted(nums, target):
    results = []
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            results.append((left, right))
            left += 1
            right -= 1
            continue
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return results if results else None
# Example usage:

nums = [1,2,3,4,5,6,7,8,9]
target = 10
result = two_sum_sorted(nums, target)
print(result)

signal.alarm(0)  # Disable the alarm