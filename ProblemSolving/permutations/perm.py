class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        import itertools
        result = []
        for perm in itertools.permutations(nums, r=len(nums)):
            result.append(perm)
        return result
        
