class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # Binary search is Half n Half. 
        # * Always check for half and choose most promising
        
        # 2 pointer technique - to memorize the indexes as we move through the array without altering the array to perform the search should be apt...
        
        # Init
        left = 0
        right = len(nums)-1
        
        # Dividing by 2 and setting pointers as we proceed
        while left < right:
            mid = (left + right)//2
            print left, mid, right
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
            
            # Smallest array condition (when the array is of length 2)
            if (right - left) == 1:
                if nums[right] == target:
                    return right
                elif nums[left] == target:
                    return left
                else:
                    return -1
    
        # Equal or single element condition
        if left == right and nums[left] == target:
            return left
            
        # no match condition
        return -1
                
        """
        # Binary search works in the below logic, existence returned
        # * Maintaining the index is not done here
        while nums:
            n = len(nums)
            mid = n//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                nums = nums[mid:]
            else:
                nums = nums[:mid]
        return False
        """
        
        """"
        # Altering same logic as above (for existence to crack)
        # * Maintaining the index left and right is a challenge
        
        start_index = 0
        
        if nums[start_index] == target:
            return 0
        
        while len(nums) > 1:
            n = len(nums)
            mid = n//2
            if nums[mid] == target:
                if (start_index + mid) < start_index:
                    return start_index - mid - 1
                else:
                    return start_index + mid
            elif nums[mid] < target:
                nums = nums[mid:]
            else:
                nums = nums[:mid] 
            start_index += mid
        return -1
        """
    
        
