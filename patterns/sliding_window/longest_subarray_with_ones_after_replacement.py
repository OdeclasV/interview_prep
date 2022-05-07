# Longest subarray with ones after replacement (hard)

####### Example #######

## Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
## Output: 6
## Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

####### END #######

def length_of_longest_substring(arr, k):
    window_start, max_length, max_ones_count = 0,0,0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1
        
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count  -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 2)