# Pending...
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       
        count = 0
        n = len(nums)
        for i in range(1,n-1):
            if nums[i] > nums[i+1] and nums[i-1] < nums[i+1]:
                count += 1
        if count > 1:
            return False
        else:
            return True
                
 
        """
        # Working half the way
        n = len(nums)
        count = 0
        for i in range(n):
            if i == n-1:
                if nums[i] >= nums[i-1] and max(nums) == nums[i]:
                    count += 1
            elif nums[i] <= nums[i+1]:
                count += 1
        if count == n-1:
            return True
        else:
            return False
        """
        
        """
        # Check for a not condition rather than a positive condition like above
        n = len(nums)
        count = 0
        for i in range(n-1):
            if nums[i]
            if nums[i] > nums[i+1]:
                count += 1
        if count > 1:
            return False
        else:
            return True
        """
        
        """
        # compare between sorted pair and the original array
        original = nums
        sort_original = sorted(nums)
        print original, sort_original
        n = len(original)
        count = 0
        i = j = 0
        while i < n:
            if original[i] != sort_original[j]:
                count += 1
                i += 1
            else:
                i += 1
                j += 1
        if count > 1:
            return False
        else:
            return True
        """
        
        """
        # Try to make it non decreasing array
        n = len(nums)
        select = None
        c = 0
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                pass
            else:
                if select is None:
                    select = i
                else:
                    nums[select],nums[i] = nums[i], nums[select]
                    select = None
                    c += 1
        if select:
            nums.append(select)
            c += 1
            
        if nums[n-1] != nums[n-2] and nums[n-1] in nums[:n-1]:
            c += 1

        if c > 1:
            return False
        else:
            return True
        """
        
        """
        n = len(nums)
        count = 0
        for i in range(n):
            #print i
            if i < n-1 and nums[i] > nums[i+1]:
                count += 1
                if count > 1:
                    break
            if i > 0 and nums[i] != nums[i-1] and nums[i] in nums[:i]:
                count += 1
                if count > 1:
                    break
            
        if count > 1:
            return False
        else:
            return True
        """
        
        # Swap and check else fail
        
        # OR if such a over rule occurs, try to delete the element and check if it is perfectly sorted
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums = nums[:i]+nums[i+1:]
                if nums == sorted(nums):
                    return True
                else:
                    return False
        return True
            
        
            
                
                
