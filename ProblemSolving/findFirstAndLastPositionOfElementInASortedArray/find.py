class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Logic: log n + already sorted demanding binary search  (ref lt sol)
        def binarySearchBounds(nums, target, bound="lower"):
            
            n = len(nums)
            l = 0
            r = n-1
            
            while l <= r:
                mid = l+(r-l)//2
                
                if nums[mid] == target:
                    if bound == "lower":
                        if mid == l or nums[mid-1] < target: # r-l == 1 then l=mid or less integer due to being sorted
                            return mid
                        r = mid-1
                    elif bound == "upper":
                        if mid == r or nums[mid+1] > target: # r-l == 1 then r=mid or greater integer due to being sorted
                            return mid
                        l = mid+1
                    else:
                        return -1
                    
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1

            return -1
        
        lb = binarySearchBounds(nums, target)
        if lb == -1:
            return [-1,-1]
        hb = binarySearchBounds(nums, target, "upper")
        
        return [lb, hb]
