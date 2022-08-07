class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        firstVal = None
        for i in range(len(nums)):
            
            if nums[i] == val:
                if firstVal == None:
                    firstVal = i
            else:
                if firstVal != None:
                    nums[i], nums[firstVal] = nums[firstVal], nums[i]
                    firstVal += 1
                
        #print(nums)
        return firstVal
    
             
