class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
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
        # Dictionary Logic - 100 pass
        count = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in count:
                count[nums[i]] = [0]
            count[nums[i]][0] += 1
            count[nums[i]].append(i)
        print count
        for key,v in count.items():
            if v[0] > 1:
                temp = v[1:]
                for i in range(len(temp)):
                    for j in range(i+1,len(temp)):
                        if abs(temp[i] - temp[j]) <= k:
                            return True
        return False
        """
    
        # Another Dictionary Logic from discussion
        
        # To track previous visited index of an entry
        prev = {}
        
        # index and element iteration
        for i, n in enumerate(nums):
            
            # checking for entry and subtract last visited
            if n in prev and i - prev[n] <= k:
                return True
            else:
            # Make an entry
                prev[n] = i
                
        return False
        
 
    

        
