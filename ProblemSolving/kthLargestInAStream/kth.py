# 100 pass - Logic to sort only initially
# * Every add will be iterated across the k length array
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        
        # initialize stream we need to use in the function
        # * We only require k elements from the start, sort once and add everything later
        self.nums = sorted(nums, reverse=True)[:k]
        self.k = k-1
    
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        # Null criteria
        if not self.nums:
            self.nums = [val]
            return val
        
        i = 0
        while i < len(self.nums) and self.nums[i] > val:
            i += 1
        
        self.nums = self.nums[:i] + [val] + self.nums[i:]
        self.nums = self.nums[:self.k+1]
            
        return self.nums[self.k]
                
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
# Pending -- time limit exceeded
# * Sorting everytime add is called doesnt make sense!
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.array = nums
        self.k = k
        self.value = 0
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        
        # Time Limit Exceeded logic otherwise all passed 
        self.array.append(val)
        if val > self.value or not self.value:
            self.array = sorted(self.array)[::-1]
            self.array = self.array[:self.k]
            self.value = self.array[-1]
        return self.value
    
    


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
"""
