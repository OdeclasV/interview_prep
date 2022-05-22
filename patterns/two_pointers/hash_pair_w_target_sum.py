"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

"""
# the difference with this approach,
# other than using a hash map,
# is that your looking for one number, Y
# that might be inside your hashmap
# each iteration gets you number X

def pair_w_target_sum(arr,target):
    nums = {}

    for i, num in enumerate(arr):

        # X + Y = Target
        # X is num, Y is (target - num)
        # if Y in hashmap, you have your pair of nums
        if (target - num) in nums:
            return [nums[target - num], i]
        else:
            nums[arr[i]] = i
    return [-1,-1]



print(pair_w_target_sum([1, 2, 3, 4, 6], 6))