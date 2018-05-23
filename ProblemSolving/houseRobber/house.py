class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Two Pointer Logic - reference from colours256 from discussions - short and simple
        
        # 2 Pointers 
        a = b = 0
        
        # Loop through the array
        for num in nums:
            
            # Track the maximum everytime a new number is considered, a being the initial value, add the number and 
            # track the maximum
            track = max(a+num,b)
            
            # In order to traverse through the array set a to b and b to current maximum
            a= b
            b= track
        
        # b will hold the maximum each time
        return b
        
        
        """
        # Track the even and odd money looted
        money_even = 0
        money_odd = 0
        maxi = -600000000
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            if i%2 == 0:
                money_even += nums[i]
            else:
                money_odd += nums[i]
        
        if money_even > money_odd:
            maxi = money_even
        else:
            maxi = money_odd
        
        if len(nums) > 2 and nums[0]+nums[-1] > maxi:
            maxi = nums[0]+nums[-1]
        
        nums.sort()
        if abs(nums.index(nums[-1])-nums.index(nums[-2])) > 1:
            if nums[-1]+nums[-2] > maxi:
                maxi = nums[-1]+nums[-2]
            
        
        return maxi
        """
        
