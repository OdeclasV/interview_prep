# Longest Substring with maximum K Distinct Characters (medium)

####### Example #######

## Input: String="araaci", K=2
## Output: 4
## Explanation: The longest substring with no more than '2' distinct characters is "araa".

####### END #######

def longest_substring_k_distinct(string,k):
    window_start = 0
    distinct_chars = {}
    max_length = 0

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in distinct_chars:
            distinct_chars[right_char] = 0
        distinct_chars[right_char] += 1

        while len(distinct_chars) > k:
            left_char = string[window_start]
            distinct_chars[left_char] -= 1
            if distinct_chars[left_char] == 0:
                del distinct_chars[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length
            



longest_substring_k_distinct("araaci", 2)