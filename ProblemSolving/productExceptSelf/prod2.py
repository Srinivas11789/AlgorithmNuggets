class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def product(nums):
            product = 1
            for element in nums:
                product *= element
            return product

        new = [1]*len(nums)
        for i in range(len(nums)):
            new[i] = product(nums[:i]+nums[i+1:])
        return new
