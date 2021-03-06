# Solution with Maintaining relative order
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # Without maintaining relative order
        """
        temp = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums[i] = nums[temp]
                nums[temp] = 0
                temp = temp - 1
            else:
                if temp == 0:
                    temp = i
        """
        # Maintaining relative order
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
            #print nums

	# Easiest thinking - just place all the non zero to front and add 0s
        lastNonZero = -1
        for i in range(len(nums)):
            if nums[i] != 0:                
                lastNonZero += 1
                nums[lastNonZero] = nums[i]
        for i in range(lastNonZero+1,len(nums)):
            nums[i] = 0
        
        
        #nums = sorted(nums)
                
