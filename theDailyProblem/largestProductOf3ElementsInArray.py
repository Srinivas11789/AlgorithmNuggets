"""
You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

Here's a starting point:

def maximum_product_of_three(lst):
  # Fill this in.

print maximum_product_of_three([-4, -4, 2, 8])
# 128
"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Logic 1: 
        # * Track 2 sorted array of length 3 for negative and positive numbers
        # * Round about logic
        # * Perform product and return max
        """
        def insert_to_array(num, array):
            # descending sorted array arrangement of 3 elements size
            if not array:
                array.append(num)
            else:
                if abs(num) >= abs(array[-1]):
                    array.append(num)
                elif abs(num) <= abs(array[0]):
                    array = [num] + array
                elif len(array) == 3 and abs(num) > abs(array[1]):
                    array = [array[0]] + [num] + [array[-1]]
                else:
                    array = [array[0]] + [num] + [array[-1]]
            print(array)
            if len(array) > 3:
                array = array[1:]
            return array

        def product(array):
            p = 1
            for n in array:
                p *= n
            return p

        def maximum_product_of_three(a):
            negative_descending = []
            positive_descending = []
            for i in range(len(a)):
                # negative number
                if a[i] < 0:
                    negative_descending = insert_to_array(a[i], negative_descending)
                else:
                    positive_descending = insert_to_array(a[i], positive_descending)
            if positive_descending:
                p_p = product(positive_descending)
            else:
                p_p = -float('inf')
            #if len(negative_descending) >= 2:
            #    if positive_descending and positive_descending[-1] > abs(negative_descending[-1]):
            #        n_p = product([positive_descending[-1], negative_descending[-1], negative_descending[-1]])
            #    else:
            #        n_p = product(negative_descending)
            #else:
            #    n_p = 0
            if negative_descending:
                n_p = product(negative_descending)
            else:
                n_p = 0
            if positive_descending and len(negative_descending) >= 2:
                np = product([positive_descending[-1], negative_descending[-1], negative_descending[-2]])
            else:
                np = -float('inf')
            print(positive_descending, negative_descending, n_p, p_p)
            return max(p_p, n_p, np)

        return maximum_product_of_three(nums)
        """
        
        # Logic 2:
        # * Use absolute value of the elements to sort
        """
        nums = sorted(nums, key=lambda x: abs(x), reverse=True)
        print(nums)
        
        # All negative elements
        if nums[0] < 0:
            return nums[0]*nums[1]*nums[2]
        
        max_product = nums[0]
        count = 1
        
        # Mix of positive and negative elements
        i = 1
        while count < 3:
            if nums[i] < 0:
                if nums[i+1] < 0 and count == 1:
                    return max_product*nums[i]*nums[i+1]
            else:
                max_product *= nums[i]
                count += 1
            i += 1
        return max_product
        """
        
        # Logic 3
        nums = sorted(nums, reverse=True)
        positive_max = nums[0]*nums[1]*nums[2]
        negative_max = nums[0]*nums[-1]*nums[-2]
        return max(positive_max, negative_max) 
                
