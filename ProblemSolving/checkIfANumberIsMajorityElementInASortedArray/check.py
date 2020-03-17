class Solution:
    # Logic 1: Using Dictionary or Counter - 100 pass - 85%
    """
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        import collections
        counts = collections.Counter(nums)
        if counts[target] > len(nums)//2:
            return True
        return False
    """
    # Logic 2: Using BST and Iteration - No dictionary - 85% faster
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def binary_search(nums, target):
            l = 0
            r = len(nums)-1
            while l < r:
                # BST
                mid = l + (r-l)//2
                if target < nums[mid]:
                    r = mid
                elif target > nums[mid]:
                    l = mid
                # Return if found
                if target == nums[l]:
                    return l
                elif target == nums[r]:
                    return r
                elif target == nums[mid]:
                    return mid
                else:
                    return -1

            return -1
        
        index = binary_search(nums, target)
        if index == -1:
            return False
        counts = 1
        left = index-1
        right = index+1
        while left >= 0 and nums[left] == target:
            counts += 1
            left -= 1
            if counts > len(nums)//2:
                return True
        while right < len(nums) and nums[right] == target:
            counts += 1
            right += 1
            if counts > len(nums)//2:
                return True
        return False
        
                
                    
            
            
