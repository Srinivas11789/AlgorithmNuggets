class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Try O(logN) as mentioned in the problem - Reference from discussion post of StefanPochmann
        
        ### Use Binary Search
        
        # Helper Function - Divide and search until you find the target
        def binarySearch(num, nums):
            
            # Initial setting of low and high
            low = 0
            high = len(nums)
            
            # Loop while you converge low < high
            while low < high:
                
                # Calculate mid
                mid = (low+high)//2
                
                # Set high and low with respect to the criteria
                if nums[mid] < num:
                    low = mid+1
                else:
                    high = mid
                
            # Return the low index that we end at,
            return low
        
        # This would search for the first occurence of the target in a sorted list
        start = binarySearch(target, nums)
        # This would search for the first occurence of the target+1 in a sorted list, which is placed 1 after the target hence subtract to find the target last index
        end = binarySearch(target+1, nums)-1

        # Binary serarch would give the index where num can be inserted in the sorted list rather than spotting it, hence ensure whether target exists in the list

        if target in nums[start:start+1]:
            return [start, end]
        else:
            return [-1,-1]
        
        
        """
        # 100 pass - nice logic but takes 2 O(N) - rethink for logn
        # Python index logic
        try:
            start = nums.index(target)
            end = len(nums) - (nums[::-1].index(target)+1)
        except:
            start = end = -1
        return [start,end]
        """
        
        
        """
        # 100 pass - O(N)
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        if result:
            if len(result) == 1:
                return (result[0],result[0])
            elif len(result) > 2:
                return (result[0],result[-1])
            else:
                return result
        else:
            return [-1,-1]
       """ 
        
        
