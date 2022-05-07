# Permutation in a string (hard)

####### Example #######

## Input: String="oidbcaf", Pattern="abc"
## Output: true
## Explanation: The string contains "bca" which is a permutation of the given pattern.

####### END #######

def permutation_in_string(string, pattern):
    window_start, matched = 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        
        if matched == len(char_frequency):
            return True
        
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    
    return False


permutation_in_string("oidbcaf", "abcabc")