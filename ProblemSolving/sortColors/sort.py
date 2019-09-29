class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # O(2N)
        
        temp = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if temp != None:
                    nums[i], nums[temp] = nums[temp], nums[i]
                    temp += 1
            else:
                if temp == None:
                    temp = i

        print(nums)
        temp1 = None
        for i in range(len(nums)):
            if nums[i] == 1:# and nums[temp1] != 0:
                if temp1 != None and nums[temp1] != 0:
                    nums[i], nums[temp1] = nums[temp1], nums[i]
                    temp1 += 1
            elif nums[i] == 2:
                if temp1 == None:
                    temp1 = i
                
        return nums
    
        """
        temp = 0
        temp1 = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[temp] = nums[temp], nums[i]
                temp += 1
                temp1 += 1
            elif nums[i] == 1:
                nums[i], nums[temp1] = nums[temp1], nums[i]
                temp1 = temp + 1
            else:
                if temp == 0:
                    temp = i
                    temp1 = temp + 1
            print nums
        return nums
        """
