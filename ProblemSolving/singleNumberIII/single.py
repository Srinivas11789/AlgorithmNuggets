class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ### List method - O(N) but the look up for count in a list might increase the iteration
        # 100 pass but runs for 2796ms faster than 1.5%
        return [i for i in nums if nums.count(i) == 1]
        # --------------------------------------------------------------------------------------
        
        ### Double Remove method
        # * For each element, remove the element from the list and also remove the same element from the list again, if not it is unique
        # * Remove element operation would take more than a linear iteration...
        # --------------------------------------------------------------------------------------
    
        ### Dictionary method 
        # - uses extra space - would always pass but that is not what we want!
        # --------------------------------------------------------------------------------------
        
        ### Exor Method
        # * Iterate through numbers, continuously exor
        # - Exor one by one, check for value change before and after
        # - If the amount added is the amount removed, then
            
                
        
    
            
        
        
        
