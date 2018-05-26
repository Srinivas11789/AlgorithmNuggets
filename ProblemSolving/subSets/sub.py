class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # Using itertools combinations - Short and easy logic - 100 pass
        import itertools
        result = []
        for i in range(len(nums)+1):
            for comb in itertools.combinations(nums,i): # use permutation when order is important as in (2,1) != (1,2)
                result.append(comb)
        return result
        
        """
        # Learn about BackTracking technique 
        # Recursion method without itertools --> Just to make sure its implementable in other languages - 100 pass
        def combinations(ans, nums):
            for i,v in enumerate(nums):
                value = ans + [v]
                result.append(value)
                combinations(value, nums[i+1:])
                
        result = [[]] # Adding the empty set as the first entry without any elements
        combinations([], nums)
        return result
        """
        
