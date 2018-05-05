class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # Doesnt work for [1,3,2,4,5] ==> when the later part of the array is sorted properly
        n = len(nums)
        result = []
        i = 0
        maxin = None
        maxi = 0
        start = None
        while i < n:
            if nums[i] > maxin or maxin is None:
                maxin = nums[i]
                maxi = i
            if i+1 <= n-1 and nums[i+1] < nums[i] and start is None:
                start = i
            i += 1
            print maxin, start
        if start is None:
            return 0
        elif start < maxi:
            return len(nums[start:maxi])
        else:
            return len(nums)
        """
        
        # sorted array
        s = sorted(nums)
        result = []
        i = 0
        start = None
        end = None
        while i < len(nums):
            if nums[i] != s[i] and start == None:
                start = i
            if nums[i] != s[i]:
                end = i
            i += 1
        #print nums[start:end], start,end, nums, s
        if start is None or end is None:
            return 0
        else:
            return len(nums[start:end+1])
                

                
                
            
                
        
