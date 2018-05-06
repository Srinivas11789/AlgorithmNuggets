class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        """
        # 100 pass - Hacky pythonic solution of splitting the array and joining
        
        n = len(nums)
        
        # K is zero
        if k == 0:
            nums
        else:
        # Forsee this, k can be any integer, make k withing length of num
            k = k%n
        
        # Rotate - assigning new values with nums[:] only works
            nums[:] = nums[n-k:]+nums[:n-k]
        """
    
        # 100 pass - Pythonic solution using pop() - which removes the last element, remove k elements from the end of the array and append then to the front of the array
        for i in range(k):
            removed = nums.pop()
            nums.insert(0,removed)
        
        
        
        
        
        
        
