"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

import math

def first_unique_char(str):
    
    char_frequency = {}
    first_index = math.inf

    for char in str:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] +=1
    
    for i in char_frequency:
        if char_frequency[i] == 1:
            char_index = str.index(i)
            first_index = min(first_index, char_index)
    
    if first_index == math.inf:
        return -1
    return first_index

print(first_unique_char("loveleetcode"))
print(first_unique_char("leetcode"))
print(first_unique_char("aabb"))