# Pending...
"""
You are given an array of integers. Return the length of the longest increasing subsequence (not necessarily contiguous) in the array.

Example:
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
"""

# Logic 1: Contiguous sub-array of increasing subsequence
def longest_increasing_subsequence(array):
    pointer = 0
    maxi = 0
    current = 0
    while pointer < len(array)-1:
        if array[pointer+1] < array[pointer]:
            maxi = max(maxi, current)
            current = 0
        else:
            current += 1
        pointer += 1
    return maxi

# Logic 1: Non Contiguous sub-array of increasing subsequence - worst case
# * Lets do recursive to go over all possible increasing subsequence
# O(N**2) 
def longest_increasing_worst_case(index, array):
    maxi_length = 1
    for i in range(index, len(array)):
        if array[i] > array[index]:
           maxi_length = max(maxi_length, 1+longest_increasing_worst_case(i, array))
    return maxi_length

def main():
    nums = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    # ANother loop as start can be any index
    maxi = 0
    for i in range(len(nums)):
        maxi = max(maxi, longest_increasing_worst_case(i, nums))
    print(maxi)
main()
