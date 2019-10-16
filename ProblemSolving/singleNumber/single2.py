    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # No Space
        nums.sort()
        freq = 1
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i+1] == nums[i]:
                freq += 1
            else:
                print(nums[i], freq)
                if freq == 1:
                    return nums[i]
                freq = 1
        return False
        
        # Extra Space
        """
        import collections
        for k,v in collections.Counter(nums).items():
            if v == 1:
                return k
        return False
        """
