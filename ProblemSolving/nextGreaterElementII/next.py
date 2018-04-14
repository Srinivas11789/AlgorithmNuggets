class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Stack based solution is the best
        
        # length of the array
        n = len(nums)
        
        # result array to store the result as -1 initially
        result = [-1]*n
        
        # Stack to store all the lesser values
        stack = []
        
        # Cool logic of using *2 in range -> will iterate i from 0-5 and again 0-5
        for i in range(n)*2:
            
            # Stack basically stores all the index of lesser elements as we traverse the array from the selected element. Once the greater element in hit the stack is flushed for all the lesser elements of the greater element until a greater than greater element is found, result is filled and greater number is added to stack and moved on the next number
            
            # If stack is filled then pop and insert hte  
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
                #print result
                
            # Else append the index to the stack
            stack.append(i)
            #print stack
        return result
 
        """
        # Logic similar to the part 1 = works but time limit exceeded
        # Result array
        result = []
        
        # iterate over the array and find the next greatest until its own position
        for i in range(len(nums)):
            select = (i + 1)%len(nums)
            # iterate from the next index until the same index is reached
            while nums[select] <= nums[i]:
                select += 1
                if select == i:
                    break
                if select >= len(nums):
                    select = select%len(nums)
            if nums[select] > nums[i]:
                great = nums[select]
            else:
                great = -1
            result.append(great)
        
        return result
        """
        
