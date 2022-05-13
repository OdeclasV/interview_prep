# fruit basket


# need to go thru avaiable fruit trees
# start my window at zero
# and keep going as long as I have no more than 2 types of fruit
# add max count of current fruits to max_num
# if more than 2, 
# shrink window and start with next item


from platform import freedesktop_os_release
import math


def max_num_of_fruits(fruitsArr):
    window_start, max_num = 0,0
    fruit_frequency = {}

    for window_end in range(len(fruitsArr)):
        right_fruit = fruitsArr[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1
    
    while len(fruit_frequency) > 2:
        left_fruit = fruitsArr[window_start]
        fruit_frequency[left_fruit] -= 1
        if fruit_frequency[left_fruit] == 0:
            del fruit_frequency[left_fruit]
        window_start += 1
    max_num = max(max_num, window_end-window_start + 1)
        
    print(fruit_frequency)
    return max_num


fruits = ['A', 'B', 'C', 'B', 'B', 'C']
print(max_num_of_fruits(fruits))
