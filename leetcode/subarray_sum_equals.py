"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,1,1], k = 2
Output: 2

"""

# going to be using sliding window approach
# my window_start is first item in array
# my window_end is item to the right of window_start
# need to iterate thru each item in array
# if my current window sum equals K
## add one to num_of_arrays var
## decrease window by one
## continue iterating with new window size
# if not
## continue iterating
# when iteration reaches last item in array
# return num_of_arrays

def sub_arr_sum(arr,k):
    window_start, num_of_subarrs = 0,0

    for window_end in range(len(arr)):
        left_item = arr[window_start]
        right_item = arr[window_end]
        if right_item == k:
            num_of_subarrs += 1
        if window_start != window_end:
            current_window_sum = left_item + right_item
            if current_window_sum == k:
                num_of_subarrs += 1
                window_start += 1
                current_window_sum -= left_item
    
    return num_of_subarrs




print(sub_arr_sum([1,-1,0], 0))