"""
You are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.

def products(nums):
  # Fill this in.

print products([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
"""

# Logic 1 with division, refresher
# O(N) to calculate the product
def nums_division(nums):
    product = 1
    for element in nums:
        product *= element
    for i in range(len(nums)):
        nums[i] = product//nums[i]
    return nums

# The most naive method (worst case)
def product(nums):
    product = 1
    for element in nums:
        product *= element
    return product

def products(nums):
    new = [1]*len(nums)
    for i in range(len(nums)):
        new[i] = product(nums[:i]+nums[i+1:])
    return new

# O(N) Method
# * Bisect the array --> moving left and right from there gives the products
# [ 1       2      3    4     5 ] 
# 2345   1345   1245  1235  1234
# Left -> Right
#   0       1     1*2  2*3  2*3*4
# 2*3*4*5  3*4*5  4*5    5    0
# Right<- Left
# O(N) + O(N) ==> O(2N) ==> O(N)
def o_of_n(nums):
    n = len(nums)
    results = [1]*n
    left = 1
    for i in range(n):
        if i > 0:
            left *= nums[i-1] 
        results[i] = left
    print(results)
    right = 1  
    for i in range(n-1, -1, -1):
        if i < n-1:
            right *= nums[i+1]
        results[i] *= right
    return results

def main():
    array = [1, 2, 3, 4, 5]
    #print(nums_division(array))
    #print(products(array))
    print(o_of_n(array))
main()    
