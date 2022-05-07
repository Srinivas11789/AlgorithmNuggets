class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # Attemp 1 - Brute Force Solution - Time limit exceeded
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                k = j + 1
                while k < n:
                    if i < j < k  and nums[i] < nums[k] < nums[j]:
                        return True
                    k += 1
                j += 1
            i += 1
        return False

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        # Logic 1: problem statement but contigously (Q wants without being cont and just i<j<k)
        """
        for i in range(1, len(nums)-1):
            
            if nums[i-1] < nums[i+1] < nums[i]:
                return True
        
        return False
        """
        
        # Logic 2: same as above but without being contiguous/adjacent
        
        def backtrack(current, nums):
            
            print(current, nums)
            
            if len(current) >= 3:
                #print(current)
                return True
        
            for i in range(len(nums)):

                if i+1 >= len(nums):
                    nxt = []
                else:
                    nxt = nums[i+1:]
    
                if len(current) == 0:
                    if nums[i] not in self.start_points:
                        if backtrack(current + [nums[i]], nxt):
                            return True
                    self.start_points.add(nums[i])
                elif len(current) == 1 and current[-1] < nums[i]: 
                    if current[0] + nums[i] not in self.second_points:
                        if backtrack(current + [nums[i]], nxt):
                            return True
                    self.second_points.add(current[0] + nums[i])
                elif len(current) == 2 and current[0] < nums[i] < current[1]:
                    return True
                
            return False

        self.start_points = set()
        self.second_points = set()
        return backtrack([], nums)
