class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def getParity(num):
            if num%2 == 0:
                return True
            return False

        if len(nums) == 1:
            return True

        for i in range(1, len(nums)):
            if getParity(nums[i-1]) == getParity(nums[i]):
                return False
        return True
        
    
