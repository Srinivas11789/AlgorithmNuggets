class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        """
        # Logic1 - Brute force - Time limit exceeded 
        for n in nums:
            if nums.count(n) > 1:
                return True
        return False
        """
        """
        # Logic2 - Sorted logic - 100 pass 
        nums = sorted(nums)
        if len(nums) > 0:
            prev = nums[0]
        else:
            return False
        for i in range(1,len(nums)):
            if prev == nums[i]:
                return True
            else:
                prev = nums[i]
        return False
        """
    
        # Logic 3 - Dictionary logic - 100 pass
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        for k,v in count.items():
            if v > 1:
                return True
        return False
