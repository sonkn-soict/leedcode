import signal
import time

TIME_LIMIT = 10
def handler(signum, frame):
    raise TimeoutError("Time limit exceeded")
signal.signal(signal.SIGALRM, handler)
signal.alarm(TIME_LIMIT)

# Sliding Window
# A window is defined by two pointers that represent the start and end of the window.
# find a length of longest substring without repeating characters
def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
s = "abcabcbb"
length = length_of_longest_substring(s)
print(length)

signal.alarm(0)  # Disable the alarm