class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Logic 1: String conversion and length ( a bit like bruteforce ) - 97% faster
        """
        result = 0
        for num in nums:
            if len(str(num))%2 == 0:
                result += 1
        return result
        """
        
        # Logic 2: ( No string conversion) Retain as Integer and perform the same - 60% faster
        # * Remove the units digits one by one until the number expires
        result = 0
        for num in nums:
            digits = 0
            while num:
                num = num//10
                digits += 1
            if digits%2 == 0:
                result += 1
        return result
