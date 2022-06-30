"""
Given a sorted array, create a new array containing squares 
of all the numbers of the input array in the sorted order.

Example:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
"""

def make_squares(arr):
    n = len(arr)
    # create new list in which every value is 0
    squares = [0 for x in range(n)]
    # used to know where biggest squared number will go in new list
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1
    return squares

print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))