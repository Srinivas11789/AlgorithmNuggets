class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        # Logic: O(N) iteration 
        
        # Control variables
        n = len(nums)
        ranges = []
        start = None
        i = 0
        
        # O(N) loop - 100 pass
        while i < n:
            # Set start 
            if start == None:
                start = i
                
            # Condition when the range is complete
            if i+1 < n and nums[i]+1 != nums[i+1]:
                # condition when range is just the same number
                if i == start:
                    ranges.append(str(nums[start]))
                else:
                    # condition when we have a range > 1
                    ranges.append(str(nums[start])+"->"+str(nums[i]))
                start = None
            
            # Condition when list comes to an end! (Similar to the one above for list end)
            if i == n-1:
                if start == None:
                    ranges.append(str(nums[i]))
                else:
                    if nums[i] == nums[i-1]+1:
                        ranges.append(str(nums[start])+"->"+str(nums[i]))
                    else:
                        ranges.append(str(nums[start]))
                    start = None
                        
            i += 1
            
        return ranges
                
                    
            
