"""
    Write a function solution that, given an integer N, returns the maximum possible value obtainable by deleting one “5” digit from the decimal representation of N. 
    It is guaranteed that N will contain at least one “5” digit. 

    Examples: 
    1. Given N = 15958, the function should return 1958. 
    2. Given N = -5859, the function should return -589.  -859 < -589
    2. Given N = -5000, the function should return -0. After deleting the “5”, the only digits in the number are zeroes, so its value is 0. 

    Assume that: 

    N is an integer within range [-999,995…999,995] 

    N contains at least one “5” digit in its decimal representation. 

    N consists of at least two digits in its decimal representation. 

    In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.  
"""


# go thru each digit in int
# if digit is 5, take it out
# if you start from left to right, assumption is that first 5 you encounter is the biggest
# stop looping once you have replaced the 5

import math

# def delete_five(number):
#     num_list = str(number)
#     temp = []
#     temp_num = num_list
#     previous_five_index  = 0

#     while '5' in num_list:
#         for i in range(len(num_list)):
#             if temp_num[i] == '5':
#                 if i > previous_five_index:
#                     num_list = num_list.replace(temp_num[i], '',1)
#                     previous_five_index = i
#                 temp.append(temp_num)
#                 break

def delete_five(N):
    if type(N) != int:
        N = int(N)
    # all_possible snumbers
    possibles = []
    # indexes of 5
    fives = []
    N = str(N)
    if "5" not in N:
        print("There must be atleast one 5")
        return int(N)
    elif len(N) < 2:
        print("Must be atleast 2 digit Number")
        return int(N)
    for i in range(0, len(N)):
        if str(N)[i] == "5":
            fives.append(i)
    print("5 found on indices = ", fives)
    for k in fives:
        chars = list(N)

        chars[k] = ''
        print("Replace {} 5 in {} and get {}".format(k, N, int("".join(chars))))
        possibles.append(int("".join(chars)))
    print("all combos = ", possibles)
    return max(possibles)

        

print(delete_five(-5859)) # 1958
#print(delete_five(-5859)) # -859
#print(delete_five(15))    # 1