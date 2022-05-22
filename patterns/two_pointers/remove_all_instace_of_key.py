"""
Given an unsorted array of numbers and a target 'key', 
remove all instances of 'key' in-place and return the new length of the array.

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
"""

def remove_element(arr,key):
    nextElement = 0 # index of next element, which is not 'key'

    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1
    
    return nextElement

print(remove_element([1, 2, 3, 6, 3, 10, 9, 3], 3))