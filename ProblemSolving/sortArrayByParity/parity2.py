class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        
        last_odd = None
        
        for i in range(len(nums)):
            
            if nums[i]%2 != 0:
                if last_odd == None:
                    last_odd = i
            else:
                print(last_odd, i)
                if last_odd == None:
                    continue
                nums[i], nums[last_odd] = nums[last_odd], nums[i]
                last_odd += 1
        
        return nums
            
