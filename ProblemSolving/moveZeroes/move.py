class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        temp = None
        for i in range(len(nums)):
            if nums[i] != 0 and temp != None:
                nums[i], nums[temp] = nums[temp], nums[i]
                temp += 1
            else:
                if temp == None and nums[i] == 0:
                    temp = i
            #print(temp, nums, i)
        #print(nums)
        return nums
