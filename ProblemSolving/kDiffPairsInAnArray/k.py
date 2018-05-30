class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Logic 2: Dictionary logic works! - access times are mich reduced
        
        # To hold the count of pairs
        result = 0
        
        # Creating a dictionary with all the count the number of occurrences
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
            
        # Drive the logic with respect to the target k
        
        # When k is less than zero, the result of i-j is absolute hence no negative values can occur
        if k < 0:
            return 0
        
        # Iterating throught the dictionary keys
        for num in count.keys():
            
            # When k == 0, k can be only zero when more than one of the same element exists
            if k == 0:
                # Its unique pairs so we do not want to decrement the number of time the pairs occur
                if count[num] > 1:
                    result += 1
            elif num+k in count:
                result += 1
        return result
        
        """
        # This doesnt work as the access times for list is much higher even though the logic works
        # Logic1: Time Limit Exceeded
        # * Using pop to extract the pairs does not work
        # * Iterating and checking for the existence of difference also does not work - unique pairs are required
        total = sum(nums)
        result = []
        
        if k < 0:
            return 0
        
        for i in range(len(nums)):
            value = k+nums[i]
            if value in nums[:i]+nums[i+1:]:
                tup = [nums[i],value]
                if tup not in result and tup[::-1] not in result:
                    result.append([nums[i],value])
        #print result
        return len(result)
        """
                
