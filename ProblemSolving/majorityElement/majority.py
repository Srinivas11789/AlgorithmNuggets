class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # Logic1: Time limit exceeded for the brute force solution
        n = len(nums)
        count = 0
        for ch in nums:
            if nums.count(ch) > n//2:
                return ch
        """ 
        
        """
        # Logic2: using hashmap - 100 pass 
        n = len(nums)
        counts = {}
        for ch in nums:
            if ch not in counts:
                counts[ch] = 0
            counts[ch] += 1
        for k,v in counts.items():
            if v > n//2:
                return k
        """
        
        # technically good solution - one liner 100pass
        return sorted(nums)[len(nums)//2]
        
            
        
        
            
