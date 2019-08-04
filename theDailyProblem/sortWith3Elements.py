"""
Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.

Example 1:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
  # Fill this in.

print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]

Challenge: Try sorting the list using constant space.
"""

def sort_3(a):
    # Constant space so add variable with element and num of time it occurs
    first = [None, 0]
    second = [None, 0]
    third = [None, 0]
    n = len(a)
    for i in range(n):
        if first[0] == None:
            first[0] = a[i]
        elif first[0] != a[i] and second[0] == None:
            second[0] = a[i]
            if second[0] < first[0]:
                first, second = second, first
        elif (second[0] != a[i] and first[0] != a[i]) and third[0] == None:
            third[0] = a[i]
            if third[0] < first[0] and third[0] < second[0]:
                first, third = third, first
                second, third = third, second
            elif third[0] < second[0]:
                second, third = third, second
        if a[i] == first[0]:
            first[1] += 1
        elif a[i] == second[0]:
            second[1] += 1
        elif a[i] == third[0]:
            third[1] += 1
        print(first, second, third)
    return [first[0]]*first[1] + [second[0]]*second[1] + [third[0]]*third[1] 
#def inbuild_3_sort(a):
#    return list(set(a))

def main():
    a = [3,3,2,1,3,2,1]
    print(sort_3(a))
    print(inbuild_3_sort(a))

main()
