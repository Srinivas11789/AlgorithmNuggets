class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Logic 1:
        # * At each house, propagate the maximum amount that can be robbed alternatively one index or 2 index.
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        max_rob = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] += max(nums[i-2] if i-2 >= 0 else 0, nums[i-3] if i-3 >=0 else 0)
            max_rob = max(max_rob, nums[i])
        print(nums)
        return max_rob
        
        # Things that wont work below! 
        
        # Thoughts 1: get max money index and calculate adjacent from there
        #maxi = max(nums)
        #huge_money = None
        #for i in range(len(nums)):
        #    if nums[i] == maxi:
        #        huge_money = i
        
        # Thoughts 2: Calculate all adjacent from the beginning
        """
        if len(nums) < 1:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(sum([nums[0],nums[-1]]) if len(nums) > 2 else 0, max(sum([nums[i] for i in range(0, len(nums), 2)]), sum([nums[i] for i in range(1, len(nums), 2)])))
        """
