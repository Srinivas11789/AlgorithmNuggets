# Pending...
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Attemp 1 - Brute Force Solution - Time limit exceeded
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                k = j + 1
                while k < n:
                    if i < j < k  and nums[i] < nums[k] < nums[j]:
                        return True
                    k += 1
                j += 1
            i += 1
        return False
    
    
    
    
    
    
    
                
                
        
