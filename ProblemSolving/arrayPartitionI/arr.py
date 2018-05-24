class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 100 pass - O(n)
        # Taking 2 numbers at a time itself, works to be n//2 or n from 2n
        # Sorting the array and moving forward ensures the maximum number that can be obtained from the operation, as the ascending order ensures that maximum number is always obtained in an operation of minumim between 2 consecutive natural numbers
        nums.sort()
        total = 0
        for i in range(0, len(nums), 2):
            total += min(nums[i],nums[i+1])
        return total
            
            
        
