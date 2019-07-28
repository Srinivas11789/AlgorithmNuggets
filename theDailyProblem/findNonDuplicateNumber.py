"""
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
Here's the function signature:

def singleNumber(nums):
  # Fill this in.

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1

Challenge: Find a way to do this using O(1) memory.
"""

def findNonDuplicateNumbers(arr):
    # Logic 0: Using dictionary or any extra space would be easy solve but the question asks to not use extra space
    
    # Logic 1: Sort and look for adjacent elements to be different, the different element is the answer
    """
    visited = None # o(1) one variable to store history
    arr.sort() # Inplace sorting
    for i in arr:
        if i != visited:
           return i
        visited = i
    return None
    """

    # Logic 2: Naive double lookup ( increasing the running time )
    """
    for i in range(len(arr)):
        if arr[i] not in arr[i+1:] and arr[i] not in arr[:i]: # this takes an extra O(N) iteration 
           return arr[i]
    return None
    """

    # Logic 3: operations (bitwise?) pending


    # Practice: Set visted elements to a negative value - this logic is a practice to get repeated elements
    for i in range(len(arr)):
        print(arr)
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")


def main():
    input = [4, 3, 2, 4, 1, 3, 2]
    print(findNonDuplicateNumbers(input))

main()
