class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import collections
        freq = list(set(collections.Counter(nums).values()))
        if not freq or (len(freq) == 1 and freq[0] == 1):
            return False
        else:
            return True
        
