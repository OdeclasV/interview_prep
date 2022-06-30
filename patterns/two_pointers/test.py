# R: string, i need longest substring of distinct chars
# I: string, only
# O: number, int (number of distinct chars)
# T: 
## what happens if empty -- output 0, or useful msg to user



# example:
## string: "aabccbb"
## output: 3

# example2:
## string: "aabccbb"
## output: 3, abc

# approach
## go thru each item in string
## make sure you save to that char in temp place, hashamp
# if that item is already in my map
# dont add it
## if not there, add it
# i need to return number of items in hashmap with onl, item = value, i to return when value =1 
# need to keep a counter, or some sort of way to count number of distinct items in hashmap to return



def distinct_chars(str):
    char_frequency = {}
    window_start = 0
    count_of_distinct_chars = 0

    if len(str) == 0:
        return 0

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        while char_frequency[right_char] > 1:
            char_frequency[right_char] -= 1
            count_of_distinct_chars = max(count_of_distinct_chars, len(char_frequency))
        print(char_frequency)

    return count_of_distinct_chars


# print(distinct_chars("aabccbb")) # 3
# print(distinct_chars("abbbb"))   # 2 
print(distinct_chars("abccde"))  # 3 abc, cde
# print(distinct_chars(""))        # 0

# example
