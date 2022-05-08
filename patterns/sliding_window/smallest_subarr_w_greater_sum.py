import math

# smallest subarray with greater sum (easy)

####### Example #######

## Input: [2, 1, 5, 2, 3, 2], S=7
## Output: 2
## Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].

####### END #######

def smallest_subarr(arr, k):
    window_sum = 0
    # set this to a infinite
    min_length = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]

        # while current window's sum is greater than k
        # shrink window by one number
        while window_sum >= k:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
        # returns 0 if no min_length subarray exists
    if min_length == math.inf:
         return 0
    return min_length


smallest_subarr([2, 1, 5, 2, 3, 2], 7)