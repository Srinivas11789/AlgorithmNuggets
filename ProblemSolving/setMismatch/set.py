class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ###### Method 0
        """
        # Time limit exceeded, everything else passed
        dup = miss = 0
        for i in range(1,len(nums)+1):
            
            if nums.count(i) == 0:
                miss = i
            
            if nums.count(i) == 2:
                dup = i
        
        return [dup,miss]
        """
        
        ###### Method 1
        """
        # Pythonic using sums
        # 100 pass - using total sum - the set sum which is unique => missing number
        
        dup = sum(nums) - sum(set(nums)) # Total sum - unique sum == number left out or duplicate
        miss = sum(range(1,len(nums)+1)) - sum(set(nums)) # total range sum - unique sum == missing number
        
        return [dup,miss]
        """
        
        ###### Method 2
        """
        # Extra array or dictionary 100 pass
        counts = {}
        dup = miss = 0
        
        for n in nums:
            
            if n not in counts:
                counts[n] = 0
            
            counts[n] += 1
        
        #print counts
        
        for i in range(1,len(nums)+1):
            
            if i not in counts:
                miss = i
            
            if i in counts and counts[i] == 2:
                dup = i
            
        return [dup, miss]
        """
        
        #### 100pass - Method 3 - Use sorting ==> you thought of sorting technique and sum technique but hesitated to implement them wondering if complexity will increase. First of all use brute force and bring about the solution in a naive manner then worry about everything else
        
        nums = sorted(nums)
        dup = 0
        miss = 1
        
        for i in range(len(nums)):
            
            if nums[i] == nums[i-1]:
                dup = nums[i]
                
            else:
                if nums[i] > nums[i-1] + 1:
                    miss = nums[i-1] + 1
            
        if nums[len(nums)-1] != len(nums):
            miss = len(nums)
            
        return [dup,miss]
        

#### Lessons learnt:
# * Analysis and learn when to use if and if vs if and else
# * static values like miss = 1 is set deliberately by the logic when a programmer writes, analyze why??
# * FIRST == BRUTEFORCE
# * Always optimize using a logic you think of, dont avoid any thoughts like sum and sort ones you thought.

        
        
