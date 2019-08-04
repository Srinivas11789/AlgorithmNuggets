"""
You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.

Here is the function signature:

def check(lst):
  # Fill this in.

print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False

Can you find a solution in O(n) time?
"""

def makeNonDecreasingWithOneChange(a):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Logic 1: Check if more than one violation is found
        # Doesnt work for 3,4,2,3
        """
        violation = 0
        n = len(a)
        for i in range(n-1):
            if a[i] > a[i+1]:
                violation += 1
            if violation > 1:
                return False
        if violation > 1:
            return False
        return True
        """
        
        # Improv Logic 1: 100 pass 85% faster
        # Improvise above logic with popping one element and checking the same condition around it (i-1 and i+2 of the pair)
        violation = 0
        n = len(a)
        for i in range(n-1):
            if a[i] > a[i+1]:
                violation += 1
            if violation > 1 or ((i-1>=0 and i+1 < n and a[i-1] > a[i+1]) and (i+2 < n and a[i] > a[i+2])) :
                return False
        return True

        
        # Logic 2 - Match remaining with sorted after the first violation ( check either way i and i+1 ) - 100 pass 25% faster
        """
        n = len(a)
        for i in range(n-1):
            if a[i] > a[i+1]:
                if a[:i]+a[i+1:] != sorted(a[:i]+a[i+1:]) and a[:i+1]+a[i+2:] != sorted(a[:i+1]+a[i+2:]):
                    return False
        return True
        """

def main():
    a = [ 13, 4, 7]
    b = [ 5, 1, 3, 2, 5]
    print(makeNonDecreasingWithOneChange(a))
    print(makeNonDecreasingWithOneChange(b))
    
main()
