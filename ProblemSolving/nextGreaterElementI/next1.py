class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        # Result array
        result = []
        
        # iterate over the first array, for each element find the index of it in the second array
        # iterate from there to find the greater number
        
        # selecting each element from the list
        for n in findNums:
            
            # index of the selected element in the nums array
            select = nums.index(n)
            
            # Setting great to -1 already is a best choice as you already handle the negative case
            great = -1
            
            # iterate from the select to the length to find mext maximum
            for i in range(select+1, len(nums)):
                
                # find the next greater number, again decision of using for or while loop was a challenge. For here helps you to iterate and keep the index within the range while the while loop otherwise might go over the max range, make a smart choice and a very easy one
                if nums[i] > nums[select]:
                    great = nums[i]
                    break
            result.append(great)
            
        return result
        
