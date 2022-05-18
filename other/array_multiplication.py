"""
Write a function solution that, given an array A of N integers (between -100 and 100), returns the sign  
(-1, 0, 1) of the product of all the numbers in the array multiplied together. Assume that N is between 1 and 1000.  
For example, given A = [1, -2, -3, 5], the function should return 1 (the multiplication equals 30).  
Given A = [1, 2, 3, -5] your function should return -1, (the multiplication equals -30). 
Given A = [1, 2, 0, -5] your function should return 0, (the multiplication equals 0). 

"""

def array_multiplication(arr):
    if len(arr) == 0:
        return None
    
    total = arr[0]

    for num in arr:
        total *= num

    if total >= 1:
        return 1
    elif total < 0:
        return -1
    else:
        return 0     

print(array_multiplication([1, -2, -3, 5])) ## 1
print(array_multiplication([1, 2, 3, -5])) ## -1
print(array_multiplication([1, 2, 0, -5])) ## 0
print(array_multiplication([1])) ## 1
print(array_multiplication([-1])) ## -1
print(array_multiplication([0])) ## 0
print(array_multiplication([])) ## None
