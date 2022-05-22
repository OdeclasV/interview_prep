"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

"""

def pair_target_sum(arr,target):
    left_pointer, right_pointer = 0, len(arr) - 1

    while left_pointer < right_pointer:
        current_sum = arr[left_pointer] + arr[right_pointer]

        if current_sum == target:
            return [left_pointer, right_pointer]

        if current_sum < target:
            left_pointer += 1 # we need a pair with a bigger sum
        else:
            right_pointer -= 1 # we need a pair with a smaller sums
    
    # if pair does not exist, return -1,-1
    return [-1,-1]

#print(pair_target_sum([1, 2, 3, 4, 6], 6))
print(pair_target_sum([2, 5, 9, 11], 12))

