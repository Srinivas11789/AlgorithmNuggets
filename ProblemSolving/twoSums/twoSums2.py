class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Logic 1: convert to dictionary and o(n) iterate
        import collections
        c = collections.Counter(nums)
        for i in range(len(nums)):
            next_element = target - nums[i]
            if next_element in c:
                for j in range(len(nums)):
                    if nums[j] == next_element and j != i:
                        return [i,j]
