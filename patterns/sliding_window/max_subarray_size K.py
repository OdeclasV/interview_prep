# maximum subarray of size K (easy)

####### Example #######

## Input: [2, 1, 5, 1, 3, 2], k=3 
## Output: 9
## Explanation: Subarray with maximum sum is [5, 1, 3].

####### END #######

def max_subarr(arr, k):
    window_start, max_sum, count = 0,0,0

    for window_end in range(len(arr)):
        right_num = arr[window_end]
        count += right_num

        # k - 1 becuase we're using index to compare
        if window_end >= k-1:
            left_num = arr[window_start]
            max_sum = max(max_sum, count)
            count -= left_num
            window_start += 1
    return max_sum

            
print(max_subarr([2, 1, 5, 1, 3, 2], 3))
print(max_subarr([2, 3, 4, 1, 5], 2))