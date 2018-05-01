class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxi = 0
        for char in nums:
            if char == 1:
                count += 1
            else:
                count = 0
            if count > maxi:
                maxi = count
        return maxi
