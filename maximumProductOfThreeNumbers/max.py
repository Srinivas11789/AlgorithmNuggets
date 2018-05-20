class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        nums.sort()
        #print nums
        
        if nums[-1] < 0 or nums[-2] < 0 or nums[-3] < 0:
            # Reversing the negative chunk
            start = end = None
        
            i = 0
        
            while i < n:
                if nums[i] < 0:
                    if start is None:
                        start = i
                    if i == n-1:
                        end = i
                else:
                    if start != None:
                        end = i
                i += 1
        
            if start != None and end != None:
                #print nums[:start],nums[start:end][::-1],nums[end:]
                nums = nums[:start]+nums[start:end][::-1]+nums[end:]
            
        #print nums, start, end
        #print nums[-1],nums[-2],nums[-3]
        
        if abs(nums[0])*abs(nums[1])*nums[-1] >  nums[-1]*nums[-2]*nums[-3]:
            return abs(nums[0])*abs(nums[1])*nums[-1]
        else:
            return nums[-1]*nums[-2]*nums[-3]
        
        
